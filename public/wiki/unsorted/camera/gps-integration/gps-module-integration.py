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