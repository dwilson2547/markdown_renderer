# SSD1306 OLED Display Communication via I2C on Raspberry Pi

Here's how to communicate with an SSD1306 OLED display via **[I2C](../3d_scanner/physical_communication_protocols/i2c.md)** from your **[Raspberry Pi](../3d_scanner/rpi_4.md)**:

## Hardware Setup

First, connect your SSD1306 OLED to the Raspberry Pi's I2C pins:

- **VCC** → 3.3V (Pin 1) or 5V (Pin 2) - check your display's voltage requirement
- **GND** → Ground (Pin 6)
- **SDA** → GPIO 2 (Pin 3) - I2C Data
- **SCL** → GPIO 3 (Pin 5) - I2C Clock

## Enable I2C on Raspberry Pi

```bash
# Enable I2C interface
sudo raspi-config
# Navigate to: Interfacing Options > I2C > Enable

# Or enable directly:
sudo systemctl enable i2c-arm

# Install I2C tools
sudo apt update
sudo apt install i2c-tools

# Detect connected I2C devices
sudo i2cdetect -y 1
```

The SSD1306 typically appears at address `0x3C` or `0x3D`.

## Install Required Python Libraries

```bash
# Install the Adafruit CircuitPython library (recommended)
pip install adafruit-circuitpython-ssd1306
pip install pillow  # For image manipulation

# Alternative: luma.oled library
pip install luma.oled
```

## Basic Usage Examples

```python
#!/usr/bin/env python3
"""
SSD1306 OLED Display Examples for Raspberry Pi
Supports both Adafruit CircuitPython and luma.oled libraries
"""

import time
import board
import busio
from PIL import Image, ImageDraw, ImageFont

# Method 1: Using Adafruit CircuitPython library
def adafruit_example():
    """Basic example using Adafruit CircuitPython SSD1306 library"""
    
    import adafruit_ssd1306
    
    # Create I2C interface
    i2c = busio.I2C(board.SCL, board.SDA)
    
    # Create SSD1306 display object
    # Common sizes: 128x64, 128x32
    display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
    
    # Clear display
    display.fill(0)
    display.show()
    
    # Create blank image for drawing
    image = Image.new("1", (display.width, display.height))
    draw = ImageDraw.Draw(image)
    
    # Draw some shapes and text
    draw.rectangle((0, 0, display.width, display.height), outline=0, fill=0)
    draw.rectangle((2, 2, display.width-2, display.height-2), outline=1, fill=0)
    draw.text((10, 10), "Hello World!", fill=1)
    draw.text((10, 25), "Raspberry Pi", fill=1)
    draw.text((10, 40), "SSD1306 OLED", fill=1)
    
    # Display image
    display.image(image)
    display.show()

def adafruit_scrolling_text():
    """Scrolling text example with Adafruit library"""
    
    import adafruit_ssd1306
    
    i2c = busio.I2C(board.SCL, board.SDA)
    display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
    
    # Load a font
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
    except:
        font = ImageFont.load_default()
    
    text = "This is a scrolling message on SSD1306 OLED display!"
    
    for i in range(len(text) * 10):
        # Create image
        image = Image.new("1", (display.width, display.height))
        draw = ImageDraw.Draw(image)
        
        # Clear image
        draw.rectangle((0, 0, display.width, display.height), outline=0, fill=0)
        
        # Calculate text position for scrolling
        x = display.width - i * 2
        draw.text((x, 20), text, font=font, fill=1)
        
        # Display
        display.image(image)
        display.show()
        time.sleep(0.1)

# Method 2: Using luma.oled library
def luma_example():
    """Basic example using luma.oled library"""
    
    from luma.core.interface.serial import i2c
    from luma.core.render import canvas
    from luma.oled.device import ssd1306
    
    # Create device
    serial = i2c(port=1, address=0x3C)
    device = ssd1306(serial, width=128, height=64)
    
    # Draw on device
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((10, 10), "Hello World!", fill="white")
        draw.text((10, 25), "Luma OLED", fill="white")
        draw.text((10, 40), "Library", fill="white")

def luma_system_stats():
    """Display system statistics using luma.oled"""
    
    from luma.core.interface.serial import i2c
    from luma.core.render import canvas
    from luma.oled.device import ssd1306
    import psutil
    import socket
    
    serial = i2c(port=1, address=0x3C)
    device = ssd1306(serial, width=128, height=64)
    
    def get_ip():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "No connection"
    
    while True:
        # Get system stats
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        ip_address = get_ip()
        
        with canvas(device) as draw:
            # CPU usage
            draw.text((0, 0), f"CPU: {cpu_percent:.1f}%", fill="white")
            
            # Memory usage
            draw.text((0, 12), f"RAM: {memory.percent:.1f}%", fill="white")
            
            # Disk usage
            draw.text((0, 24), f"Disk: {disk.percent:.1f}%", fill="white")
            
            # IP Address
            draw.text((0, 36), f"IP: {ip_address}", fill="white")
            
            # Temperature (if available)
            try:
                temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
                draw.text((0, 48), f"Temp: {temp:.1f}°C", fill="white")
            except:
                draw.text((0, 48), "Temp: N/A", fill="white")
        
        time.sleep(2)

# Comprehensive OLED class for easy use
class SSD1306Display:
    """Easy-to-use SSD1306 OLED display class"""
    
    def __init__(self, width=128, height=64, address=0x3C):
        import adafruit_ssd1306
        
        self.width = width
        self.height = height
        
        # Initialize I2C and display
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.display = adafruit_ssd1306.SSD1306_I2C(width, height, self.i2c, addr=address)
        
        # Load default font
        try:
            self.font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
        except:
            self.font = ImageFont.load_default()
        
        self.clear()
    
    def clear(self):
        """Clear the display"""
        self.display.fill(0)
        self.display.show()
    
    def text(self, x, y, text, font=None):
        """Display text at specified coordinates"""
        image = Image.new("1", (self.width, self.height))
        draw = ImageDraw.Draw(image)
        
        if font is None:
            font = self.font
            
        draw.text((x, y), text, font=font, fill=1)
        self.display.image(image)
        self.display.show()
    
    def multi_line_text(self, lines, font=None):
        """Display multiple lines of text"""
        image = Image.new("1", (self.width, self.height))
        draw = ImageDraw.Draw(image)
        
        if font is None:
            font = self.font
        
        y_offset = 0
        line_height = 12
        
        for line in lines:
            draw.text((0, y_offset), line, font=font, fill=1)
            y_offset += line_height
        
        self.display.image(image)
        self.display.show()
    
    def progress_bar(self, x, y, width, height, progress):
        """Draw a progress bar (progress: 0.0 to 1.0)"""
        image = Image.new("1", (self.width, self.height))
        draw = ImageDraw.Draw(image)
        
        # Outer rectangle
        draw.rectangle((x, y, x + width, y + height), outline=1, fill=0)
        
        # Progress fill
        fill_width = int(width * progress)
        if fill_width > 0:
            draw.rectangle((x + 1, y + 1, x + fill_width - 1, y + height - 1), outline=1, fill=1)
        
        self.display.image(image)
        self.display.show()

# Example usage
if __name__ == "__main__":
    print("SSD1306 OLED Display Examples")
    print("Make sure your display is connected to I2C pins")
    
    try:
        # Test basic functionality
        print("Testing basic display...")
        adafruit_example()
        time.sleep(3)
        
        # Test the easy-to-use class
        print("Testing custom class...")
        oled = SSD1306Display()
        
        # Display some text
        oled.multi_line_text([
            "Raspberry Pi",
            "OLED Display",
            "Working!",
            "IP: 192.168.1.100"
        ])
        time.sleep(3)
        
        # Show progress bar
        for i in range(101):
            oled.clear()
            oled.text(0, 0, "Loading...")
            oled.progress_bar(0, 20, 100, 10, i/100.0)
            oled.text(0, 40, f"{i}%")
            time.sleep(0.05)
        
        print("Demo complete!")
        
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure I2C is enabled and display is connected properly")
```

## Advanced Features

```python
#!/usr/bin/env python3
"""
Advanced SSD1306 OLED Display Features
Including animations, graphics, and real-time data display
"""

import time
import math
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import threading
import queue

class AdvancedOLEDDisplay:
    """Advanced SSD1306 display with animations and graphics"""
    
    def __init__(self, width=128, height=64, address=0x3C):
        self.width = width
        self.height = height
        
        # Initialize I2C and display
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.display = adafruit_ssd1306.SSD1306_I2C(width, height, self.i2c, addr=address)
        
        # Fonts
        try:
            self.small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
            self.medium_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
            self.large_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
        except:
            self.small_font = ImageFont.load_default()
            self.medium_font = ImageFont.load_default()
            self.large_font = ImageFont.load_default()
        
        self.clear()
        
        # Animation control
        self.animation_running = False
        self.animation_thread = None
    
    def clear(self):
        """Clear the display"""
        self.display.fill(0)
        self.display.show()
    
    def draw_bitmap(self, bitmap_data, x=0, y=0):
        """Draw a bitmap image"""
        image = Image.new("1", (self.width, self.height))
        draw = ImageDraw.Draw(image)
        
        for row, byte_row in enumerate(bitmap_data):
            for col, pixel in enumerate(byte_row):
                if pixel:
                    draw.point((x + col, y + row), fill=1)
        
        self.display.image(image)
        self.display.show()
    
    def bouncing_ball_animation(self, duration=10):
        """Animated bouncing ball"""
        start_time = time.time()
        
        # Ball properties
        ball_x, ball_y = 20, 20
        vel_x, vel_y = 3, 2
        ball_size = 4
        
        while time.time() - start_time < duration:
            # Create image
            image = Image.new("1", (self.width, self.height))
            draw = ImageDraw.Draw(image)
            
            # Update ball position
            ball_x += vel_x
            ball_y += vel_y
            
            # Bounce off walls
            if ball_x <= ball_size or ball_x >= self.width - ball_size:
                vel_x = -vel_x
            if ball_y <= ball_size or ball_y >= self.height - ball_size:
                vel_y = -vel_y
            
            # Keep ball in bounds
            ball_x = max(ball_size, min(self.width - ball_size, ball_x))
            ball_y = max(ball_size, min(self.height - ball_size, ball_y))
            
            # Draw ball
            draw.ellipse((ball_x - ball_size, ball_y - ball_size, 
                         ball_x + ball_size, ball_y + ball_size), 
                        outline=1, fill=1)
            
            # Draw borders
            draw.rectangle((0, 0, self.width-1, self.height-1), outline=1)
            
            self.display.image(image)
            self.display.show()
            time.sleep(0.05)
    
    def sine_wave_animation(self, duration=10):
        """Animated sine wave"""
        start_time = time.time()
        phase = 0
        
        while time.time() - start_time < duration:
            image = Image.new("1", (self.width, self.height))
            draw = ImageDraw.Draw(image)
            
            # Draw sine wave
            points = []
            for x in range(self.width):
                y = int(self.height/2 + 20 * math.sin(2 * math.pi * x / 40 + phase))
                points.append((x, y))
            
            # Draw the wave
            for i in range(len(points) - 1):
                draw.line([points[i], points[i+1]], fill=1)
            
            # Add labels
            draw.text((5, 5), "Sine Wave", font=self.small_font, fill=1)
            draw.text((5, self.height-15), f"Phase: {phase:.1f}", font=self.small_font, fill=1)
            
            phase += 0.2
            
            self.display.image(image)
            self.display.show()
            time.sleep(0.1)
    
    def digital_clock(self, duration=30):
        """Digital clock display"""
        start_time = time.time()
        
        while time.time() - start_time < duration:
            image = Image.new("1", (self.width, self.height))
            draw = ImageDraw.Draw(image)
            
            # Get current time
            current_time = time.strftime("%H:%M:%S")
            current_date = time.strftime("%Y-%m-%d")
            day_of_week = time.strftime("%A")
            
            # Draw time (large)
            draw.text((10, 15), current_time, font=self.large_font, fill=1)
            
            # Draw date (small)
            draw.text((10, 40), current_date, font=self.small_font, fill=1)
            draw.text((10, 52), day_of_week, font=self.small_font, fill=1)
            
            # Draw border
            draw.rectangle((0, 0, self.width-1, self.height-1), outline=1)
            
            self.display.image(image)
            self.display.show()
            time.sleep(1)
    
    def temperature_gauge(self, temperature, min_temp=-10, max_temp=50):
        """Display temperature as a gauge"""
        image = Image.new("1", (self.width, self.height))
        draw = ImageDraw.Draw(image)
        
        # Gauge properties
        center_x, center_y = self.width // 2, self.height - 10
        radius = 40
        
        # Calculate angle based on temperature
        temp_range = max_temp - min_temp
        temp_ratio = (temperature - min_temp) / temp_range
        angle = math.pi + (temp_ratio * math.pi)  # From π to 2π
        
        # Draw gauge arc
        gauge_points = []
        for i in range(50):
            a = math.pi + (i * math.pi / 49)
            x = center_x + radius * math.cos(a)
            y = center_y + radius * math.sin(a)
            gauge_points.append((int(x), int(y)))
        
        # Draw gauge outline
        for i in range(len(gauge_points) - 1):
            draw.line([gauge_points[i], gauge_points[i+1]], fill=1)
        
        # Draw temperature needle
        needle_x = center_x + (radius - 5) * math.cos(angle)
        needle_y = center_y + (radius - 5) * math.sin(angle)
        draw.line([(center_x, center_y), (int(needle_x), int(needle_y))], fill=1)
        
        # Draw center dot
        draw.ellipse((center_x-2, center_y-2, center_x+2, center_y+2), fill=1)
        
        # Temperature text
        draw.text((center_x-20, 5), f"{temperature:.1f}°C", font=self.medium_font, fill=1)
        
        # Min/max labels
        draw.text((5, center_y-5), f"{min_temp}", font=self.small_font, fill=1)
        draw.text((self.width-20, center_y-5), f"{max_temp}", font=self.small_font, fill=1)
        
        self.display.image(image)
        self.display.show()
    
    def scrolling_menu(self, menu_items, selected_index=0):
        """Display a scrolling menu"""
        image = Image.new("1", (self.width, self.height))
        draw = ImageDraw.Draw(image)
        
        # Menu properties
        line_height = 12
        visible_lines = self.height // line_height
        
        # Calculate scroll offset
        if selected_index >= visible_lines:
            scroll_offset = selected_index - visible_lines + 1
        else:
            scroll_offset = 0
        
        # Draw menu items
        for i, item in enumerate(menu_items[scroll_offset:scroll_offset + visible_lines]):
            y = i * line_height
            actual_index = i + scroll_offset
            
            # Highlight selected item
            if actual_index == selected_index:
                draw.rectangle((0, y, self.width, y + line_height), fill=1)
                draw.text((5, y + 2), item, font=self.small_font, fill=0)
            else:
                draw.text((5, y + 2), item, font=self.small_font, fill=1)
        
        # Draw scroll indicator
        if len(menu_items) > visible_lines:
            scroll_height = self.height
            indicator_height = max(5, scroll_height * visible_lines // len(menu_items))
            indicator_y = scroll_height * scroll_offset // len(menu_items)
            
            draw.rectangle((self.width-3, indicator_y, self.width-1, 
                          indicator_y + indicator_height), fill=1)
        
        self.display.image(image)
        self.display.show()
    
    def draw_graph(self, data_points, title="Graph", min_val=None, max_val=None):
        """Draw a line graph"""
        if not data_points:
            return
        
        image = Image.new("1", (self.width, self.height))
        draw = ImageDraw.Draw(image)
        
        # Graph area
        graph_x = 10
        graph_y = 15
        graph_width = self.width - 15
        graph_height = self.height - 25
        
        # Auto-scale if not provided
        if min_val is None:
            min_val = min(data_points)
        if max_val is None:
            max_val = max(data_points)
        
        if max_val == min_val:
            max_val = min_val + 1  # Avoid division by zero
        
        # Draw title
        draw.text((5, 2), title, font=self.small_font, fill=1)
        
        # Draw axes
        draw.line([(graph_x, graph_y), (graph_x, graph_y + graph_height)], fill=1)  # Y-axis
        draw.line([(graph_x, graph_y + graph_height), (graph_width, graph_y + graph_height)], fill=1)  # X-axis
        
        # Draw data points
        points = []
        for i, value in enumerate(data_points):
            x = graph_x + (i * (graph_width - graph_x) // len(data_points))
            y = graph_y + graph_height - int((value - min_val) * graph_height / (max_val - min_val))
            points.append((x, y))
        
        # Draw lines between points
        for i in range(len(points) - 1):
            draw.line([points[i], points[i+1]], fill=1)
        
        # Draw value labels
        draw.text((2, graph_y), f"{max_val:.0f}", font=self.small_font, fill=1)
        draw.text((2, graph_y + graph_height - 8), f"{min_val:.0f}", font=self.small_font, fill=1)
        
        self.display.image(image)
        self.display.show()

# Example usage and demonstrations
def demo_advanced_features():
    """Demonstrate advanced OLED features"""
    
    print("Starting advanced OLED demonstrations...")
    oled = AdvancedOLEDDisplay()
    
    try:
        # Digital clock
        print("Showing digital clock for 10 seconds...")
        oled.digital_clock(duration=10)
        
        # Temperature gauge
        print("Showing temperature gauge...")
        for temp in range(-5, 35, 2):
            oled.temperature_gauge(temp)
            time.sleep(0.5)
        
        # Bouncing ball animation
        print("Bouncing ball animation...")
        oled.bouncing_ball_animation(duration=8)
        
        # Sine wave animation
        print("Sine wave animation...")
        oled.sine_wave_animation(duration=8)
        
        # Menu demo
        print("Menu demonstration...")
        menu_items = ["Option 1", "Option 2", "Option 3", "Settings", "About", "Exit"]
        for selected in range(len(menu_items)):
            oled.scrolling_menu(menu_items, selected)
            time.sleep(1)
        
        # Graph demo
        print("Graph demonstration...")
        import random
        data = [random.randint(10, 90) for _ in range(20)]
        oled.draw_graph(data, "Random Data")
        time.sleep(5)
        
        print("Demo complete!")
        oled.clear()
        
    except KeyboardInterrupt:
        print("Demo interrupted by user")
        oled.clear()
    except Exception as e:
        print(f"Error during demo: {e}")
        oled.clear()

if __name__ == "__main__":
    demo_advanced_features()
```

## Troubleshooting Tips

1. **Display not detected:**
   ```bash
   # Check I2C address
   sudo i2cdetect -y 1
   
   # If nothing appears, check connections and try:
   sudo i2cdetect -y 0  # For older Pi models
   ```

2. **Wrong address:**
   - Most SSD1306 displays use `0x3C`, but some use `0x3D`
   - Try both addresses in your code

3. **Display appears scrambled:**
   - Check if you have the correct width/height (128x64 vs 128x32)
   - Verify power supply (3.3V vs 5V requirement)

4. **Permission errors:**
   ```bash
   # Add user to i2c group
   sudo usermod -a -G i2c $USER
   # Logout and login again
   ```

## Quick Test Script

```python
#!/usr/bin/env python3
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw

# Quick test
i2c = busio.I2C(board.SCL, board.SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

display.fill(0)
display.show()

image = Image.new("1", (128, 64))
draw = ImageDraw.Draw(image)
draw.text((0, 0), "OLED Working!", fill=1)

display.image(image)
display.show()
```

The examples above provide everything you need to get started with your SSD1306 OLED display, from basic text display to advanced animations and real-time data visualization!