# Interfacing GY-521 MPU-6050 IMU Module with Raspberry Pi

You can interface with a GY-521 MPU-6050 IMU module using **[I2C](../3d_scanner/physical_communication_protocols/i2c.md)** communication on a **[Raspberry Pi](../3d_scanner/rpi_4.md)**. Here's how to set it up:

## Hardware Connections

Connect the MPU-6050 to your Raspberry Pi's GPIO pins:
- **VCC** → 3.3V (Pin 1 or 17)
- **GND** → Ground (Pin 6, 9, 14, 20, 25, 30, 34, or 39)
- **SCL** → GPIO 3 (Pin 5) - I2C Clock
- **SDA** → GPIO 2 (Pin 3) - I2C Data
- **XDA** and **XCL** → Leave unconnected (unless using auxiliary I2C)
- **AD0** → Ground (sets I2C address to 0x68) or 3.3V (for 0x69)
- **INT** → Optional GPIO pin for interrupt functionality

## Software Setup

First, enable I2C on your Raspberry Pi:
```bash
sudo raspi-config
```
Navigate to "Interfacing Options" → "I2C" → "Yes"

Install required Python libraries:
```bash
sudo apt update
sudo apt install python3-smbus python3-pip
pip3 install mpu6050-raspberrypi
```

## Basic Python Code

Here's a simple example to read data from the MPU-6050:

```python
import smbus
import math
import time

# MPU-6050 registers
MPU6050_ADDR = 0x68
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47

# Initialize I2C bus
bus = smbus.SMBus(1)  # Use bus 1 for newer Pi models

# Wake up the MPU-6050
bus.write_byte_data(MPU6050_ADDR, PWR_MGMT_1, 0)

def read_word_2c(addr):
    """Read 16-bit signed value from two registers"""
    high = bus.read_byte_data(MPU6050_ADDR, addr)
    low = bus.read_byte_data(MPU6050_ADDR, addr + 1)
    val = (high << 8) + low
    return val - 65536 if val >= 0x8000 else val

def get_accel_data():
    """Get accelerometer data in g's"""
    accel_x = read_word_2c(ACCEL_XOUT_H) / 16384.0
    accel_y = read_word_2c(ACCEL_YOUT_H) / 16384.0
    accel_z = read_word_2c(ACCEL_ZOUT_H) / 16384.0
    return accel_x, accel_y, accel_z

def get_gyro_data():
    """Get gyroscope data in degrees/second"""
    gyro_x = read_word_2c(GYRO_XOUT_H) / 131.0
    gyro_y = read_word_2c(GYRO_YOUT_H) / 131.0
    gyro_z = read_word_2c(GYRO_ZOUT_H) / 131.0
    return gyro_x, gyro_y, gyro_z

# Main loop
try:
    while True:
        accel = get_accel_data()
        gyro = get_gyro_data()
        
        print(f"Accel: X={accel[0]:.2f}g, Y={accel[1]:.2f}g, Z={accel[2]:.2f}g")
        print(f"Gyro: X={gyro[0]:.2f}°/s, Y={gyro[1]:.2f}°/s, Z={gyro[2]:.2f}°/s")
        print("-" * 50)
        
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nExiting...")
```

## Using a Library (Easier Option)

Alternatively, use the `mpu6050-raspberrypi` library:

```python
from mpu6050 import mpu6050
import time

# Initialize sensor
sensor = mpu6050(0x68)

try:
    while True:
        # Get accelerometer data
        accel_data = sensor.get_accel_data()
        print(f"Accel: X={accel_data['x']:.2f}, Y={accel_data['y']:.2f}, Z={accel_data['z']:.2f}")
        
        # Get gyroscope data
        gyro_data = sensor.get_gyro_data()
        print(f"Gyro: X={gyro_data['x']:.2f}, Y={gyro_data['y']:.2f}, Z={gyro_data['z']:.2f}")
        
        # Get temperature
        temp = sensor.get_temp()
        print(f"Temperature: {temp:.2f}°C")
        print("-" * 50)
        
        time.sleep(1)
except KeyboardInterrupt:
    print("\nExiting...")
```

## Troubleshooting

- Check connections with `i2cdetect -y 1` - you should see device at 0x68 or 0x69
- Ensure I2C is enabled in raspi-config
- Use 3.3V, not 5V, to avoid damaging the Pi
- Add pull-up resistors (4.7kΩ) on SDA and SCL lines if you experience communication issues

The MPU-6050 provides 3-axis accelerometer and gyroscope data, plus temperature readings, making it excellent for motion sensing, orientation detection, and basic IMU applications.