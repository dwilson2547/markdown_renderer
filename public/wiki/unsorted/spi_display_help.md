Yes, this is a common issue with SPI displays! The mirroring is caused by the memory access control settings. Here are several ways to fix it:

## Option 1: Use the rotation parameter

Try different rotation values in your ST7789 initialization:

```python
# Try different rotation values: 0, 90, 180, 270
disp = st7789.ST7789(spi, cs=cs_pin, dc=dc_pin, rst=reset_pin,
                     width=320, height=480, rotation=180)  # Try 180 first
```

## Option 2: Flip the image in Python before displaying

```python
from PIL import Image, ImageDraw, ImageOps

# Create your image as normal
image = Image.new('RGB', (320, 480))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, 320, 480), fill=(255, 0, 0))
draw.text((50, 50), "Hello World!", fill=(255, 255, 255))

# Flip the image horizontally (mirror fix)
image = ImageOps.mirror(image)

# Or flip vertically if needed
# image = ImageOps.flip(image)

# Or both
# image = ImageOps.mirror(ImageOps.flip(image))

disp.image(image)
```

## Option 3: Modify the memory access control directly

If you need more control, you can send the memory access control command directly:

```python
import digitalio
import board
from PIL import Image, ImageDraw
import adafruit_rgb_display.st7789 as st7789

# Your normal setup
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D24)
reset_pin = digitalio.DigitalInOut(board.D25)
spi = board.SPI()

disp = st7789.ST7789(spi, cs=cs_pin, dc=dc_pin, rst=reset_pin,
                     width=320, height=480, rotation=0)

# Send memory access control command to fix mirroring
# This command controls how the display memory is accessed
disp._write(0x36, bytes([0x00]))  # Try different values:
# 0x00 - Normal
# 0x40 - Vertical flip  
# 0x80 - Horizontal flip
# 0xC0 - Both flips
# 0x20 - Different orientation
# 0x60 - Different orientation + vertical flip
# 0xA0 - Different orientation + horizontal flip
# 0xE0 - Different orientation + both flips

# Now display your image normally
image = Image.new('RGB', (320, 480))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, 320, 480), fill=(255, 0, 0))
draw.text((50, 50), "Hello World!", fill=(255, 255, 255))
disp.image(image)
```

## Quick Test Method

The easiest way to test is to create an asymmetric image and try different solutions:

```python
# Create a test image that's clearly asymmetric
image = Image.new('RGB', (320, 480))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, 320, 480), fill=(0, 0, 0))  # Black background
draw.rectangle((10, 10, 100, 50), fill=(255, 0, 0))  # Red rectangle top-left
draw.text((10, 60), "TOP LEFT", fill=(255, 255, 255))
draw.text((200, 400), "BOTTOM RIGHT", fill=(255, 255, 255))

# Try this first - most common fix
image = ImageOps.mirror(image)
disp.image(image)
```

Try **Option 2** (ImageOps.mirror) first as it's the simplest and most commonly fixes the mirroring issue. If that doesn't work, experiment with the rotation parameter or the memory access control values.

Which direction is your image mirrored - horizontally (left-right flipped) or vertically (upside down)?