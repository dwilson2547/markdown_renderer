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