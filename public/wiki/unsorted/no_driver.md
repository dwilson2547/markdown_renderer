You're right - I apologize for the confusion. The ST7796 isn't directly supported in those common libraries. Let me give you working alternatives:

## Option 1: Use ST7789 Driver (Most Compatible)

The ST7796 is very similar to ST7789, and this often works:

```bash
pip3 install adafruit-circuitpython-rgb-display pillow
```

```python
import digitalio
import board
from PIL import Image, ImageDraw
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS and DC pins
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D24)
reset_pin = digitalio.DigitalInOut(board.D25)

# Setup SPI bus
spi = board.SPI()

# Create the display (try ST7789 driver with ST7796 dimensions)
disp = st7789.ST7789(spi, cs=cs_pin, dc=dc_pin, rst=reset_pin,
                     width=320, height=480, rotation=0)

# Test it
image = Image.new('RGB', (320, 480))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, 320, 480), fill=(255, 0, 0))
draw.text((50, 50), "Hello World!", fill=(255, 255, 255))
disp.image(image)
```

## Option 2: Pure Python SPI Implementation

If the ST7789 driver doesn't work, here's a complete Python-only solution:

```python
import spidev
import RPi.GPIO as GPIO
from PIL import Image
import time
import numpy as np

class ST7796:
    def __init__(self):
        # GPIO pins
        self.DC = 24
        self.RST = 25
        
        # Setup GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.DC, GPIO.OUT)
        GPIO.setup(self.RST, GPIO.OUT)
        
        # Setup SPI
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 32000000
        
        self.width = 320
        self.height = 480
        
        self.init_display()
    
    def write_cmd(self, cmd):
        GPIO.output(self.DC, GPIO.LOW)
        self.spi.writebytes([cmd])
    
    def write_data(self, data):
        GPIO.output(self.DC, GPIO.HIGH)
        if isinstance(data, list):
            self.spi.writebytes(data)
        else:
            self.spi.writebytes([data])
    
    def init_display(self):
        # Reset
        GPIO.output(self.RST, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(self.RST, GPIO.HIGH)
        time.sleep(0.1)
        
        # ST7796 initialization sequence
        self.write_cmd(0x01)  # Software reset
        time.sleep(0.15)
        
        self.write_cmd(0x11)  # Sleep out
        time.sleep(0.25)
        
        self.write_cmd(0x3A)  # Pixel format
        self.write_data(0x55)  # 16-bit color
        
        self.write_cmd(0x36)  # Memory access control
        self.write_data(0x48)  # RGB order
        
        self.write_cmd(0x29)  # Display on
        time.sleep(0.15)
    
    def set_window(self, x0, y0, x1, y1):
        self.write_cmd(0x2A)  # Column address set
        self.write_data([x0 >> 8, x0 & 0xFF, x1 >> 8, x1 & 0xFF])
        
        self.write_cmd(0x2B)  # Row address set
        self.write_data([y0 >> 8, y0 & 0xFF, y1 >> 8, y1 & 0xFF])
        
        self.write_cmd(0x2C)  # Memory write
    
    def display_image(self, image):
        # Convert PIL image to RGB565 format
        if image.size != (self.width, self.height):
            image = image.resize((self.width, self.height))
        
        rgb_image = image.convert('RGB')
        pixels = np.array(rgb_image)
        
        # Convert to RGB565
        r = (pixels[:,:,0] >> 3) << 11
        g = (pixels[:,:,1] >> 2) << 5
        b = pixels[:,:,2] >> 3
        rgb565 = r | g | b
        
        # Set full screen window
        self.set_window(0, 0, self.width-1, self.height-1)
        
        # Send pixel data
        pixel_bytes = []
        for row in rgb565:
            for pixel in row:
                pixel_bytes.extend([pixel >> 8, pixel & 0xFF])
        
        # Send in chunks to avoid memory issues
        chunk_size = 4096
        GPIO.output(self.DC, GPIO.HIGH)
        for i in range(0, len(pixel_bytes), chunk_size):
            self.spi.writebytes(pixel_bytes[i:i+chunk_size])

# Usage example
if __name__ == "__main__":
    display = ST7796()
    
    # Create test image
    image = Image.new('RGB', (320, 480))
    draw = ImageDraw.Draw(image)
    
    # Draw something
    draw.rectangle((0, 0, 320, 480), fill=(0, 0, 255))  # Blue background
    draw.rectangle((50, 50, 270, 100), fill=(255, 255, 255))  # White rectangle
    draw.text((60, 60), "Hello ST7796!", fill=(0, 0, 0))
    
    # Display it
    display.display_image(image)
    
    print("Image displayed! Press Ctrl+C to exit.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
```

## Option 3: Try ILI9341 Driver

Sometimes the ILI9341 driver works with ST7796:

```python
import adafruit_rgb_display.ili9341 as ili9341
# Use same connection code as ST7789 example above, but replace st7789 with ili9341
```

Try Option 1 first (ST7789), and if that doesn't work properly, use Option 2 (pure Python implementation). The pure Python version gives you complete control and should definitely work with your ST7796 display.