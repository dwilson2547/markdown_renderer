# Reading GPS Coordinates on Raspberry Pi Pico with MicroPython

Yes, absolutely! You can connect a **GPS module** to your **[Raspberry Pi Pico](rpi-pico.md)** and read GPS coordinates. Here's how to do it with MicroPython:

## Hardware Setup

Most GPS modules use **[UART (serial)](../3d_scanner/physical_communication_protocols/uart.md)** communication. Common modules include:
- **NEO-6M**, **NEO-8M** (popular and affordable)
- **NEO-9M** (newer, faster acquisition)

### Wiring Example (NEO-6M to Pico):
```
GPS Module    →    Raspberry Pi Pico
VCC           →    3.3V (Pin 36)
GND           →    GND (Pin 38)
TX            →    GP1 (Pin 2) - Pico RX
RX            →    GP0 (Pin 1) - Pico TX
```

## Basic MicroPython Code

Here's a complete example to read GPS coordinates:

```python
import machine
import time

# Initialize UART for GPS
gps_uart = machine.UART(0, baudrate=9600, tx=machine.Pin(0), rx=machine.Pin(1))

def parse_gps_data(data):
    """Parse NMEA sentences and extract coordinates"""
    lines = data.split('\n')
    
    for line in lines:
        if line.startswith('$GPGGA') or line.startswith('$GNGGA'):
            # Parse GGA sentence (Global Positioning System Fix Data)
            parts = line.split(',')
            
            if len(parts) >= 15 and parts[2] and parts[4]:  # Check if we have valid data
                # Latitude
                lat_raw = parts[2]
                lat_dir = parts[3]
                if lat_raw and lat_dir:
                    lat_deg = float(lat_raw[:2])
                    lat_min = float(lat_raw[2:])
                    latitude = lat_deg + (lat_min / 60.0)
                    if lat_dir == 'S':
                        latitude = -latitude
                
                # Longitude  
                lon_raw = parts[4]
                lon_dir = parts[5]
                if lon_raw and lon_dir:
                    lon_deg = float(lon_raw[:3])
                    lon_min = float(lon_raw[3:])
                    longitude = lon_deg + (lon_min / 60.0)
                    if lon_dir == 'W':
                        longitude = -longitude
                
                # Number of satellites
                satellites = parts[7] if parts[7] else "0"
                
                # Altitude
                altitude = parts[9] if parts[9] else "0"
                
                return {
                    'latitude': latitude,
                    'longitude': longitude,
                    'satellites': int(satellites),
                    'altitude': float(altitude),
                    'fix': True
                }
    
    return {'fix': False}

def main():
    print("GPS Reader Starting...")
    print("Waiting for GPS fix...")
    
    buffer = ""
    
    while True:
        if gps_uart.any():
            try:
                # Read available data
                data = gps_uart.read().decode('utf-8')
                buffer += data
                
                # Process complete lines
                while '\n' in buffer:
                    line, buffer = buffer.split('\n', 1)
                    
                    # Parse GPS data from complete sentences
                    gps_info = parse_gps_data(line + '\n')
                    
                    if gps_info['fix']:
                        print(f"Latitude: {gps_info['latitude']:.6f}")
                        print(f"Longitude: {gps_info['longitude']:.6f}")
                        print(f"Satellites: {gps_info['satellites']}")
                        print(f"Altitude: {gps_info['altitude']:.1f}m")
                        print("-" * 40)
                        
            except UnicodeDecodeError:
                # Skip invalid characters
                pass
        
        time.sleep(0.1)

if __name__ == "__main__":
    main()
```

## Advanced Version with Error Handling

```python
import machine
import time
import select
import sys

class GPSReader:
    def __init__(self, uart_id=0, tx_pin=0, rx_pin=1, baudrate=9600):
        self.uart = machine.UART(uart_id, baudrate=baudrate, 
                                tx=machine.Pin(tx_pin), rx=machine.Pin(rx_pin))
        self.buffer = ""
        self.last_fix = None
        
    def read_gps(self):
        """Read and parse GPS data"""
        if self.uart.any():
            try:
                data = self.uart.read().decode('utf-8')
                self.buffer += data
                
                # Process complete NMEA sentences
                while '\r\n' in self.buffer:
                    sentence, self.buffer = self.buffer.split('\r\n', 1)
                    self._parse_sentence(sentence)
                    
            except UnicodeDecodeError:
                pass
    
    def _parse_sentence(self, sentence):
        """Parse individual NMEA sentence"""
        if sentence.startswith('$GPGGA') or sentence.startswith('$GNGGA'):
            self._parse_gga(sentence)
        elif sentence.startswith('$GPRMC') or sentence.startswith('$GNRMC'):
            self._parse_rmc(sentence)
    
    def _parse_gga(self, sentence):
        """Parse GGA sentence (detailed fix data)"""
        parts = sentence.split(',')
        
        if len(parts) >= 15 and parts[2] and parts[4] and parts[6] != '0':
            try:
                # Convert coordinates
                lat = self._convert_coordinate(parts[2], parts[3])
                lon = self._convert_coordinate(parts[4], parts[5])
                
                self.last_fix = {
                    'latitude': lat,
                    'longitude': lon,
                    'satellites': int(parts[7]) if parts[7] else 0,
                    'altitude': float(parts[9]) if parts[9] else 0.0,
                    'time': parts[1],
                    'quality': int(parts[6]),
                    'timestamp': time.time()
                }
                
            except (ValueError, IndexError):
                pass
    
    def _convert_coordinate(self, raw_coord, direction):
        """Convert NMEA coordinate to decimal degrees"""
        if not raw_coord:
            return 0.0
            
        # Determine if latitude (2 digits) or longitude (3 digits)
        if len(raw_coord) >= 4:
            if '.' in raw_coord:
                decimal_pos = raw_coord.index('.')
                if decimal_pos >= 4:  # Longitude
                    degrees = float(raw_coord[:3])
                    minutes = float(raw_coord[3:])
                else:  # Latitude
                    degrees = float(raw_coord[:2])
                    minutes = float(raw_coord[2:])
            else:
                return 0.0
        else:
            return 0.0
        
        decimal_degrees = degrees + (minutes / 60.0)
        
        if direction in ['S', 'W']:
            decimal_degrees = -decimal_degrees
            
        return decimal_degrees
    
    def get_location(self):
        """Get the most recent GPS fix"""
        self.read_gps()
        return self.last_fix
    
    def has_fix(self):
        """Check if we have a recent GPS fix"""
        if self.last_fix is None:
            return False
        # Consider fix valid if less than 10 seconds old
        return (time.time() - self.last_fix['timestamp']) < 10

# Main program
def main():
    gps = GPSReader()
    print("GPS Reader initialized")
    print("Waiting for GPS fix... (This may take 30-60 seconds outdoors)")
    
    last_print = 0
    
    while True:
        # Check for user input (optional)
        if select.select([sys.stdin], [], [], 0)[0]:
            command = input().strip().lower()
            if command == 'quit':
                break
        
        location = gps.get_location()
        
        # Print status every 2 seconds
        if time.time() - last_print > 2:
            if gps.has_fix() and location:
                print(f"Lat: {location['latitude']:.6f}, Lon: {location['longitude']:.6f}")
                print(f"Satellites: {location['satellites']}, Alt: {location['altitude']:.1f}m")
                print(f"GPS Time: {location['time']}")
            else:
                print("Searching for GPS satellites...")
            
            last_print = time.time()
        
        time.sleep(0.1)

if __name__ == "__main__":
    main()
```

## Important Notes

### Hardware Considerations
- **GPS modules need clear sky view** - won't work indoors reliably
- **Cold start can take 30-60 seconds** to get first fix
- **Check your GPS module's specifications** - some use different UART pins or baud rates
- **Power consumption** - GPS modules can be power-hungry

### Software Considerations
- **NMEA sentences** - GPS modules output various sentence types (GGA, RMC, etc.)
- **Coordinate conversion** - NMEA format uses degrees and decimal minutes
- **Error handling** - GPS data can be incomplete or corrupted

## Testing Tips

1. **Start outdoors** with clear sky view
2. **LED indicators** - Some modules have LED indicators for fix status
3. **Raw data testing** - You can test with a serial terminal first to see raw NMEA data
4. **Backup battery** - Consider adding one to GPS module for faster subsequent fixes

## Next Steps

Would you like me to show you how to:
- Integrate this with sending coordinates over USB serial to your computer?
- Add logging capabilities?
- Calculate distances between coordinates?
- Add specific features like waypoint navigation?