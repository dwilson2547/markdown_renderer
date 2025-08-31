# Adding GPS EXIF Data to Raspberry Pi Camera Images

To add GPS EXIF data to images captured with **[picamera2](../3d_scanner/sensors/rpi_cam_module_v2_8mp.md)**, you'll need to use the `exif` parameter in your capture method and format the GPS coordinates properly. Here's how you can do it:

## Install Required Packages

First, make sure you have the necessary packages:

```bash
pip install exif piexif
```

## Basic Implementation

Here's a complete example showing how to add GPS EXIF data:

```python
#!/usr/bin/env python3
import time
import piexif
from picamera2 import Picamera2
from fractions import Fraction

def decimal_to_dms(decimal_degrees):
    """
    Convert decimal degrees to degrees, minutes, seconds format for EXIF
    Returns tuple of ((degrees, 1), (minutes, 1), (seconds, 100))
    """
    degrees = int(abs(decimal_degrees))
    minutes_float = (abs(decimal_degrees) - degrees) * 60
    minutes = int(minutes_float)
    seconds = (minutes_float - minutes) * 60
    
    # Convert to rational numbers (fractions) as required by EXIF
    return ((degrees, 1), (minutes, 1), (int(seconds * 100), 100))

def create_gps_exif(latitude, longitude, altitude=None):
    """
    Create GPS EXIF data dictionary
    latitude: decimal degrees (positive for North, negative for South)
    longitude: decimal degrees (positive for East, negative for West)  
    altitude: meters above sea level (optional)
    """
    
    # Determine hemisphere references
    lat_ref = 'N' if latitude >= 0 else 'S'
    lon_ref = 'E' if longitude >= 0 else 'W'
    
    # Convert to DMS format
    lat_dms = decimal_to_dms(latitude)
    lon_dms = decimal_to_dms(longitude)
    
    gps_dict = {
        piexif.GPSIFD.GPSLatitudeRef: lat_ref,
        piexif.GPSIFD.GPSLatitude: lat_dms,
        piexif.GPSIFD.GPSLongitudeRef: lon_ref,
        piexif.GPSIFD.GPSLongitude: lon_dms,
        piexif.GPSIFD.GPSMapDatum: "WGS-84",
    }
    
    # Add altitude if provided
    if altitude is not None:
        alt_ref = 0 if altitude >= 0 else 1  # 0 = above sea level, 1 = below
        gps_dict[piexif.GPSIFD.GPSAltitudeRef] = alt_ref
        gps_dict[piexif.GPSIFD.GPSAltitude] = (int(abs(altitude) * 100), 100)
    
    return gps_dict

def capture_image_with_gps(latitude, longitude, altitude=None, filename="image_with_gps.jpg"):
    """
    Capture an image with GPS EXIF data using PiCamera2
    """
    
    # Initialize camera
    picam2 = Picamera2()
    
    # Configure camera (you can adjust these settings as needed)
    config = picam2.create_still_configuration()
    picam2.configure(config)
    
    # Start camera
    picam2.start()
    
    # Allow camera to warm up
    time.sleep(2)
    
    try:
        # Create GPS EXIF data
        gps_exif = create_gps_exif(latitude, longitude, altitude)
        
        # Create complete EXIF dictionary
        exif_dict = {
            "0th": {},
            "Exif": {},
            "GPS": gps_exif,
            "1st": {},
            "thumbnail": None
        }
        
        # Convert to bytes
        exif_bytes = piexif.dump(exif_dict)
        
        # Capture image with EXIF data
        picam2.capture_file(filename, exif=exif_bytes)
        
        print(f"Image captured with GPS data: {filename}")
        print(f"Location: {latitude}, {longitude}")
        if altitude:
            print(f"Altitude: {altitude}m")
            
    finally:
        # Clean up
        picam2.stop()

# Example usage with real GPS coordinates
if __name__ == "__main__":
    # Example coordinates (Big Ben, London)
    lat = 51.5007
    lon = -0.1246
    alt = 11  # meters above sea level
    
    # Capture image with GPS data
    capture_image_with_gps(lat, lon, alt, "photo_with_location.jpg")
    
    # You can also capture without altitude
    capture_image_with_gps(lat, lon, filename="photo_basic_gps.jpg")
```

## Getting Real GPS Coordinates

If you want to get actual GPS coordinates from a GPS module, here's how you can integrate it:

```python
#!/usr/bin/env python3
import serial
import pynmea2
import time
from picamera2 import Picamera2
import piexif
from fractions import Fraction

class GPSReader:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600):
        """
        Initialize GPS reader for NMEA GPS modules
        Common ports: /dev/ttyUSB0, /dev/ttyAMA0, /dev/serial0
        """
        self.ser = serial.Serial(port, baudrate, timeout=1)
        
    def get_gps_data(self, timeout=30):
        """
        Read GPS data until we get a valid fix
        Returns: (latitude, longitude, altitude) or None if timeout
        """
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            try:
                line = self.ser.readline().decode('ascii', errors='replace').strip()
                
                if line.startswith('$GPGGA') or line.startswith('$GNGGA'):
                    msg = pynmea2.parse(line)
                    
                    if msg.latitude and msg.longitude:
                        lat = float(msg.latitude)
                        lon = float(msg.longitude)
                        
                        # Convert from NMEA format if needed
                        if msg.lat_dir == 'S':
                            lat = -lat
                        if msg.lon_dir == 'W':
                            lon = -lon
                            
                        # Altitude (convert from string to float if available)
                        alt = float(msg.altitude) if msg.altitude else None
                        
                        return lat, lon, alt
                        
            except (pynmea2.ParseError, ValueError, UnicodeDecodeError):
                continue
                
        return None
    
    def close(self):
        self.ser.close()

def capture_with_live_gps(filename="gps_photo.jpg"):
    """
    Capture photo with live GPS data from connected GPS module
    """
    gps = GPSReader()  # Adjust port if needed
    
    print("Waiting for GPS fix...")
    gps_data = gps.get_gps_data(timeout=60)
    
    if gps_data:
        lat, lon, alt = gps_data
        print(f"GPS fix acquired: {lat}, {lon}, altitude: {alt}m")
        
        # Use the previous capture function
        capture_image_with_gps(lat, lon, alt, filename)
        
    else:
        print("Could not get GPS fix within timeout period")
        
    gps.close()

# Alternative: Using gpsd daemon (if you have it set up)
def get_gps_from_gpsd():
    """
    Alternative method using gpsd daemon
    Requires: pip install gpsd-py3
    """
    try:
        import gpsd
        
        # Connect to the local gpsd
        gpsd.connect()
        
        # Get a GPS reading
        packet = gpsd.get_current()
        
        if packet.mode >= 2:  # 2D fix or better
            return packet.lat, packet.lon, packet.alt if packet.mode >= 3 else None
        else:
            return None
            
    except ImportError:
        print("gpsd-py3 not installed. Use: pip install gpsd-py3")
        return None
    except Exception as e:
        print(f"GPS error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Method 1: Using direct serial connection to GPS module
    # capture_with_live_gps("live_gps_photo.jpg")
    
    # Method 2: Using gpsd (uncomment if you have gpsd running)
    # gps_data = get_gps_from_gpsd()
    # if gps_data:
    #     lat, lon, alt = gps_data
    #     capture_image_with_gps(lat, lon, alt, "gpsd_photo.jpg")
    
    pass
```

## Key Points

1. **EXIF Format**: GPS coordinates in EXIF must be in degrees/minutes/seconds format with rational numbers (fractions), not decimal degrees.

2. **PiCamera2 Integration**: Use the `exif` parameter in `capture_file()` method to embed the EXIF data.

3. **Required Packages**: 
   - `piexif` for creating EXIF data
   - `pynmea2` for parsing GPS NMEA sentences (if using GPS module)
   - `pyserial` for GPS module communication

4. **GPS Module Connection**: Most USB GPS modules appear as `/dev/ttyUSB0`. For GPIO-connected modules, try `/dev/ttyAMA0` or `/dev/serial0`.

## Testing the EXIF Data

You can verify the GPS data was embedded correctly:

```python
# Test script to read EXIF data
import piexif
from PIL import Image

def read_gps_exif(filename):
    img = Image.open(filename)
    exif_dict = piexif.load(img.info['exif'])
    
    if 'GPS' in exif_dict:
        gps_data = exif_dict['GPS']
        print("GPS EXIF data found:")
        for key, value in gps_data.items():
            print(f"  {piexif.GPSIFD(key).name}: {value}")
    else:
        print("No GPS data found in EXIF")

# Test your captured image
read_gps_exif("photo_with_location.jpg")
```

The GPS data will then be visible in photo viewers and mapping applications that support EXIF GPS data.