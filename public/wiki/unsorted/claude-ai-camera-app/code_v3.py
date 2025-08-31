#!/usr/bin/env python3
"""
Raspberry Pi Camera Application with GPS and Manual Controls
Requirements:
- pip install picamera2 pygame gpsd-py3 pillow piexif
- Enable camera and SPI interfaces via raspi-config
- Install and configure gpsd for GPS module
"""

import pygame
import sys
import time
import threading
from datetime import datetime
import os
import json
import numpy as np
from pathlib import Path
from typing import Optional, Dict, Any

try:
    from picamera2 import Picamera2, Preview
    from picamera2.encoders import H264Encoder
    from picamera2.outputs import FileOutput
    import piexif
    from PIL import Image
    import gpsd
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Install with: pip install picamera2 pygame gpsd-py3 pillow piexif")
    sys.exit(1)

class GPSHandler:
    """Handle GPS data collection"""
    
    def __init__(self):
        self.connected = False
        self.last_position = None
        self.connect()
    
    def connect(self):
        """Connect to GPS daemon"""
        try:
            gpsd.connect()
            self.connected = True
            print("GPS connected")
        except Exception as e:
            print(f"GPS connection failed: {e}")
            self.connected = False
    
    def get_position(self) -> Optional[Dict[str, float]]:
        """Get current GPS position"""
        if not self.connected:
            return self.last_position
            
        try:
            packet = gpsd.get_current()
            if packet.mode >= 2:  # 2D fix or better
                position = {
                    'latitude': packet.lat,
                    'longitude': packet.lon,
                    'altitude': getattr(packet, 'alt', 0),
                    'timestamp': datetime.utcnow().isoformat()
                }
                self.last_position = position
                return position
        except Exception as e:
            print(f"GPS read error: {e}")
        
        return self.last_position

class CameraApp:
    """Main camera application"""
    
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        
        # Display settings for ST7796U 320x480
        self.DISPLAY_WIDTH = 320
        self.DISPLAY_HEIGHT = 480
        self.screen = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        pygame.display.set_caption("Pi Camera")
        
        # Initialize camera
        self.camera = Picamera2()
        self.setup_camera()
        
        # GPS handler
        self.gps = GPSHandler()
        
        # App state
        self.running = True
        self.low_power_mode = False
        self.preview_enabled = True
        self.recording = False
        self.current_mode = "auto"  # auto, manual
        
        # UI state
        self.menu_visible = False
        self.current_menu = "main"
        self.selected_option = 0
        
        # Manual camera settings
        self.manual_settings = {
            'shutter_speed': 1000,  # microseconds
            'iso': 100,
            'brightness': 0.0,
            'contrast': 1.0,
            'saturation': 1.0,
            'sharpness': 1.0,
            'exposure_compensation': 0
        }
        
        # Create output directories
        self.photo_dir = Path("photos")
        self.video_dir = Path("videos")
        self.photo_dir.mkdir(exist_ok=True)
        self.video_dir.mkdir(exist_ok=True)
        
        # Font for UI
        self.font = pygame.font.Font(None, 24)
        self.small_font = pygame.font.Font(None, 18)
        
        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.GRAY = (128, 128, 128)
        
        # Menu definitions
        self.menus = {
            "main": ["Take Photo", "Record Video", "Settings", "Power Mode", "Exit"],
            "settings": ["Camera Mode", "Manual Settings", "GPS Info", "Back"],
            "manual": ["Shutter Speed", "ISO", "Brightness", "Contrast", "Back"],
            "camera_mode": ["Auto Mode", "Manual Mode", "Back"]
        }
        
        # Clock for frame rate control
        self.clock = pygame.time.Clock()
        
    def setup_camera(self):
        """Initialize camera configuration"""
        # Configure camera for preview and capture
        preview_config = self.camera.create_preview_configuration(
            main={"size": (320, 240)},
            lores={"size": (320, 240), "format": "YUV420"}
        )
        
        still_config = self.camera.create_still_configuration(
            main={"size": (4056, 3040)},  # Full resolution for Pi Camera v2
            lores={"size": (320, 240), "format": "YUV420"}
        )
        
        video_config = self.camera.create_video_configuration(
            main={"size": (1920, 1080)},
            lores={"size": (320, 240), "format": "YUV420"}
        )
        
        # Start with preview configuration
        self.camera.configure(preview_config)
        self.camera.start()
        
    def apply_manual_settings(self):
        """Apply manual camera settings"""
        if self.current_mode == "manual":
            controls = {}
            
            # Convert settings to camera controls
            if self.manual_settings['shutter_speed'] > 0:
                controls['ExposureTime'] = self.manual_settings['shutter_speed']
                controls['AeEnable'] = False
            else:
                controls['AeEnable'] = True
                
            controls['AnalogueGain'] = self.manual_settings['iso'] / 100.0
            controls['Brightness'] = self.manual_settings['brightness']
            controls['Contrast'] = self.manual_settings['contrast']
            controls['Saturation'] = self.manual_settings['saturation']
            controls['Sharpness'] = self.manual_settings['sharpness']
            
            self.camera.set_controls(controls)
    
    def capture_photo(self):
        """Capture a photo with GPS data"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.photo_dir / f"photo_{timestamp}.jpg"
        
        # Get GPS position
        gps_data = self.gps.get_position()
        
        # Configure for high-resolution capture
        still_config = self.camera.create_still_configuration(
            main={"size": (4056, 3040)},
            lores={"size": (320, 240), "format": "YUV420"}
        )
        
        self.camera.switch_mode_and_capture_file(still_config, str(filename))
        
        # Add GPS EXIF data if available
        if gps_data:
            self.add_gps_exif(filename, gps_data)
        
        print(f"Photo saved: {filename}")
        return filename
    
    def add_gps_exif(self, image_path: Path, gps_data: Dict[str, float]):
        """Add GPS data to image EXIF"""
        try:
            # Load existing EXIF data
            exif_dict = piexif.load(str(image_path))
            
            # Convert GPS coordinates to EXIF format
            def decimal_to_dms(decimal_degrees):
                """Convert decimal degrees to degrees, minutes, seconds"""
                degrees = int(abs(decimal_degrees))
                minutes = int((abs(decimal_degrees) - degrees) * 60)
                seconds = int(((abs(decimal_degrees) - degrees) * 60 - minutes) * 60 * 100)
                return [(degrees, 1), (minutes, 1), (seconds, 100)]
            
            # GPS data
            gps_ifd = {
                piexif.GPSIFD.GPSLatitudeRef: 'N' if gps_data['latitude'] >= 0 else 'S',
                piexif.GPSIFD.GPSLatitude: decimal_to_dms(gps_data['latitude']),
                piexif.GPSIFD.GPSLongitudeRef: 'E' if gps_data['longitude'] >= 0 else 'W',
                piexif.GPSIFD.GPSLongitude: decimal_to_dms(gps_data['longitude']),
                piexif.GPSIFD.GPSAltitudeRef: 0,
                piexif.GPSIFD.GPSAltitude: (int(abs(gps_data['altitude']) * 100), 100),
                piexif.GPSIFD.GPSTimeStamp: (
                    (datetime.utcnow().hour, 1),
                    (datetime.utcnow().minute, 1),
                    (datetime.utcnow().second, 1)
                )
            }
            
            exif_dict['GPS'] = gps_ifd
            
            # Save image with GPS data
            exif_bytes = piexif.dump(exif_dict)
            piexif.insert(exif_bytes, str(image_path))
            
        except Exception as e:
            print(f"Failed to add GPS EXIF data: {e}")
    
    def start_recording(self):
        """Start video recording"""
        if self.recording:
            return
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.video_dir / f"video_{timestamp}.mp4"
        
        # Configure for video recording
        video_config = self.camera.create_video_configuration(
            main={"size": (1920, 1080)},
            lores={"size": (320, 240), "format": "YUV420"}
        )
        
        self.camera.configure(video_config)
        encoder = H264Encoder(bitrate=10000000)
        self.camera.start_recording(encoder, str(filename))
        
        self.recording = True
        print(f"Recording started: {filename}")
    
    def stop_recording(self):
        """Stop video recording"""
        if not self.recording:
            return
            
        self.camera.stop_recording()
        self.recording = False
        print("Recording stopped")
        
        # Return to preview mode
        preview_config = self.camera.create_preview_configuration(
            main={"size": (320, 240)},
            lores={"size": (320, 240), "format": "YUV420"}
        )
        self.camera.configure(preview_config)
    
    def toggle_power_mode(self):
        """Toggle between normal and low power mode"""
        self.low_power_mode = not self.low_power_mode
        self.preview_enabled = not self.low_power_mode
        
        if self.low_power_mode:
            print("Low power mode enabled")
        else:
            print("Normal power mode")
    
    def handle_input(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.menu_visible:
                        self.menu_visible = False
                    else:
                        self.running = False
                        
                elif event.key == pygame.K_SPACE:  # Menu toggle
                    self.menu_visible = not self.menu_visible
                    self.current_menu = "main"
                    self.selected_option = 0
                    
                elif event.key == pygame.K_RETURN:  # Take photo (when menu not visible)
                    if not self.menu_visible:
                        self.capture_photo()
                        
                elif event.key == pygame.K_r:  # Record toggle
                    if not self.menu_visible:
                        if self.recording:
                            self.stop_recording()
                        else:
                            self.start_recording()
                            
                elif event.key == pygame.K_p:  # Power mode toggle
                    if not self.menu_visible:
                        self.toggle_power_mode()
                
                # Menu navigation
                elif self.menu_visible:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.menus[self.current_menu])
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.menus[self.current_menu])
                    elif event.key == pygame.K_RETURN:
                        self.handle_menu_selection()
    
    def handle_menu_selection(self):
        """Handle menu item selection"""
        current_items = self.menus[self.current_menu]
        selected_item = current_items[self.selected_option]
        
        if self.current_menu == "main":
            if selected_item == "Take Photo":
                self.capture_photo()
                self.menu_visible = False
            elif selected_item == "Record Video":
                if self.recording:
                    self.stop_recording()
                else:
                    self.start_recording()
                self.menu_visible = False
            elif selected_item == "Settings":
                self.current_menu = "settings"
                self.selected_option = 0
            elif selected_item == "Power Mode":
                self.toggle_power_mode()
                self.menu_visible = False
            elif selected_item == "Exit":
                self.running = False
                
        elif self.current_menu == "settings":
            if selected_item == "Camera Mode":
                self.current_menu = "camera_mode"
                self.selected_option = 0
            elif selected_item == "Manual Settings":
                self.current_menu = "manual"
                self.selected_option = 0
            elif selected_item == "GPS Info":
                self.show_gps_info()
            elif selected_item == "Back":
                self.current_menu = "main"
                self.selected_option = 0
                
        elif self.current_menu == "camera_mode":
            if selected_item == "Auto Mode":
                self.current_mode = "auto"
                self.camera.set_controls({'AeEnable': True, 'AwbEnable': True})
            elif selected_item == "Manual Mode":
                self.current_mode = "manual"
                self.apply_manual_settings()
            elif selected_item == "Back":
                self.current_menu = "settings"
                self.selected_option = 0
                
        elif self.current_menu == "manual":
            if selected_item == "Back":
                self.current_menu = "settings"
                self.selected_option = 0
            else:
                self.adjust_manual_setting(selected_item)
    
    def adjust_manual_setting(self, setting_name):
        """Adjust manual camera setting"""
        # This would typically open a submenu or slider
        # For simplicity, we'll cycle through preset values
        
        if setting_name == "Shutter Speed":
            speeds = [100, 500, 1000, 2000, 5000, 10000, 20000, 50000]
            current_idx = speeds.index(self.manual_settings['shutter_speed']) if self.manual_settings['shutter_speed'] in speeds else 0
            self.manual_settings['shutter_speed'] = speeds[(current_idx + 1) % len(speeds)]
            
        elif setting_name == "ISO":
            isos = [100, 200, 400, 800, 1600]
            current_idx = isos.index(self.manual_settings['iso']) if self.manual_settings['iso'] in isos else 0
            self.manual_settings['iso'] = isos[(current_idx + 1) % len(isos)]
            
        self.apply_manual_settings()
    
    def show_gps_info(self):
        """Display GPS information"""
        gps_data = self.gps.get_position()
        if gps_data:
            print(f"GPS: Lat {gps_data['latitude']:.6f}, Lon {gps_data['longitude']:.6f}")
        else:
            print("GPS: No position available")
    
    def draw_preview(self):
        """Draw camera preview"""
        if not self.preview_enabled:
            self.screen.fill(self.BLACK)
            text = self.font.render("Low Power Mode", True, self.WHITE)
            text_rect = text.get_rect(center=(self.DISPLAY_WIDTH//2, self.DISPLAY_HEIGHT//2))
            self.screen.blit(text, text_rect)
            return
        
        try:
            # Get camera array and convert to pygame surface
            array = self.camera.capture_array("lores")
            
            # Handle different array formats
            if len(array.shape) == 3 and array.shape[2] == 3:
                # RGB format - swap axes for pygame
                surface = pygame.surfarray.make_surface(array.swapaxes(0, 1))
            elif len(array.shape) == 2:
                # Grayscale format - convert to RGB
                # Create RGB array by repeating grayscale values
                rgb_array = np.stack([array, array, array], axis=2)
                surface = pygame.surfarray.make_surface(rgb_array.swapaxes(0, 1))
            else:
                # YUV420 or other format - create surface from luminance
                if len(array.shape) == 3:
                    # Take first channel (luminance)
                    luma = array[:, :, 0]
                    rgb_array = np.stack([luma, luma, luma], axis=2)
                    surface = pygame.surfarray.make_surface(rgb_array.swapaxes(0, 1))
                else:
                    # Fallback - create blank surface
                    surface = pygame.Surface((array.shape[1], array.shape[0]))
                    surface.fill(self.GRAY)
            
            # Scale to fit display (maintain aspect ratio)
            preview_height = 360  # Leave room for status bar
            scaled_surface = pygame.transform.scale(surface, (self.DISPLAY_WIDTH, preview_height))
            self.screen.blit(scaled_surface, (0, 0))
            
        except Exception as e:
            # Fallback - fill with gray
            self.screen.fill(self.GRAY)
            error_text = self.small_font.render(f"Preview Error: {str(e)[:30]}", True, self.WHITE)
            self.screen.blit(error_text, (10, 10))
    
    def draw_status_bar(self):
        """Draw status information"""
        y_offset = self.DISPLAY_HEIGHT - 120
        
        # Background for status
        status_rect = pygame.Rect(0, y_offset, self.DISPLAY_WIDTH, 120)
        pygame.draw.rect(self.screen, (0, 0, 0, 128), status_rect)
        
        # Status information
        status_lines = [
            f"Mode: {self.current_mode.upper()}",
            f"Power: {'LOW' if self.low_power_mode else 'NORMAL'}",
            f"Recording: {'YES' if self.recording else 'NO'}",
            f"GPS: {'OK' if self.gps.last_position else 'NO FIX'}"
        ]
        
        for i, line in enumerate(status_lines):
            color = self.GREEN if i == 3 and self.gps.last_position else self.WHITE
            text = self.small_font.render(line, True, color)
            self.screen.blit(text, (10, y_offset + 10 + i * 20))
        
        # Manual settings display
        if self.current_mode == "manual":
            settings_text = f"SS:{self.manual_settings['shutter_speed']}μs ISO:{self.manual_settings['iso']}"
            text = self.small_font.render(settings_text, True, self.WHITE)
            self.screen.blit(text, (10, y_offset + 90))
    
    def draw_menu(self):
        """Draw menu overlay"""
        if not self.menu_visible:
            return
        
        # Semi-transparent background
        overlay = pygame.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(180)
        self.screen.blit(overlay, (0, 0))
        
        # Menu items
        menu_items = self.menus[self.current_menu]
        menu_height = len(menu_items) * 40
        start_y = (self.DISPLAY_HEIGHT - menu_height) // 2
        
        for i, item in enumerate(menu_items):
            y = start_y + i * 40
            color = self.GREEN if i == self.selected_option else self.WHITE
            
            # Highlight selected item
            if i == self.selected_option:
                highlight_rect = pygame.Rect(20, y - 5, self.DISPLAY_WIDTH - 40, 35)
                pygame.draw.rect(self.screen, (50, 50, 150), highlight_rect)
            
            text = self.font.render(item, True, color)
            self.screen.blit(text, (30, y))
    
    def draw_controls_help(self):
        """Draw control help text"""
        if self.menu_visible:
            return
        
        help_lines = [
            "SPACE: Menu",
            "ENTER: Photo",
            "R: Record",
            "P: Power Mode",
            "ESC: Exit"
        ]
        
        for i, line in enumerate(help_lines):
            text = self.small_font.render(line, True, self.WHITE)
            self.screen.blit(text, (self.DISPLAY_WIDTH - 120, 10 + i * 16))
    
    def run(self):
        """Main application loop"""
        print("Camera app started")
        print("Controls: SPACE=Menu, ENTER=Photo, R=Record, P=Power, ESC=Exit")
        
        try:
            while self.running:
                # Handle input
                self.handle_input()
                
                # Clear screen
                self.screen.fill(self.BLACK)
                
                # Draw preview
                self.draw_preview()
                
                # Draw UI elements
                self.draw_status_bar()
                self.draw_controls_help()
                self.draw_menu()
                
                # Update display
                pygame.display.flip()
                
                # Control frame rate (lower in low power mode)
                fps = 10 if self.low_power_mode else 30
                self.clock.tick(fps)
                
        except KeyboardInterrupt:
            print("\nShutting down...")
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Clean up resources"""
        if self.recording:
            self.stop_recording()
        
        self.camera.stop()
        self.camera.close()
        pygame.quit()
        print("Cleanup complete")

def main():
    """Main entry point"""
    try:
        app = CameraApp()
        app.run()
    except Exception as e:
        print(f"Application error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())