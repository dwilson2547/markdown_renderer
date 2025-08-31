# How to Collect Data from TOF400C VL53L1X Sensors on Raspberry Pi

To collect data from TOF400C VL53L1X sensors on your **[Raspberry Pi](../3d_scanner/rpi_4.md)**, you'll need to set up **[I2C](../3d_scanner/physical_communication_protocols/i2c.md)** communication and use appropriate libraries. Here's how to get started:

## Hardware Setup

1. **Connect the sensors via I2C:**
   - VCC → 3.3V (Pin 1)
   - GND → Ground (Pin 6)
   - SDA → GPIO 2 (Pin 3)
   - SCL → GPIO 3 (Pin 5)

2. **For multiple sensors:** You'll need to change their I2C addresses or use GPIO pins to control the XSHUT (shutdown) pins to enable them one at a time.

## Software Setup

1. **Enable I2C on your Pi:**
   ```bash
   sudo raspi-config
   # Navigate to Interface Options > I2C > Enable
   ```

2. **Install required packages:**
   ```bash
   sudo apt update
   sudo apt install python3-pip i2c-tools
   pip3 install adafruit-circuitpython-vl53l1x
   ```

3. **Verify sensor detection:**
   ```bash
   i2cdetect -y 1
   # Should show device at address 0x29
   ```

## Basic Python Code

Here's a simple script to read distance data:

```python
import time
import board
import busio
import adafruit_vl53l1x

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize sensor
vl53 = adafruit_vl53l1x.VL53L1X(i2c)

# Start ranging
vl53.start_ranging()

try:
    while True:
        if vl53.data_ready:
            distance = vl53.distance
            print(f"Distance: {distance} cm")
            vl53.clear_interrupt()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Stopping...")
finally:
    vl53.stop_ranging()
```

## For Multiple Sensors

If you need multiple sensors, you can either:
- Use different I2C addresses by setting them programmatically
- Use GPIO pins to control XSHUT pins and enable sensors individually
- Use an I2C multiplexer

Would you like me to elaborate on any of these approaches or help with a specific configuration?