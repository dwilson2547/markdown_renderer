#!/usr/bin/env python3
"""
RGB565 to BRG655 Color Converter

RGB565 format: RRRRRGGGGGGBBBBB (5 bits red, 6 bits green, 5 bits blue)
BRG655 format: BBBBBRRRRRRGGGG (5 bits blue, 6 bits red, 5 bits green)

This script converts between the two formats by rearranging: Blue-Red-Green with adjusted bit widths.
"""

def rgb565_to_brg655(rgb565_color):
    """
    Convert RGB565 color to BRG655 format
    
    Args:
        rgb565_color (int): 16-bit RGB565 color value
    
    Returns:
        int: 16-bit BRG655 color value
    """
    # Extract individual color components from RGB565
    red = (rgb565_color >> 11) & 0x1F    # Upper 5 bits
    green = (rgb565_color >> 5) & 0x3F   # Middle 6 bits  
    blue = rgb565_color & 0x1F           # Lower 5 bits
    
    # Scale red from 5 bits to 6 bits (multiply by 2 to expand range)
    red_6bit = (red << 1) | (red >> 4)   # Duplicate MSB to fill 6th bit
    
    # Scale green from 6 bits to 5 bits (divide by 2 to compress range)
    green_5bit = green >> 1
    
    # Reconstruct as BRG655: Blue(5) Red(6) Green(5)
    brg655_color = (blue << 11) | (red_6bit << 5) | green_5bit
    
    return brg655_color

def brg655_to_rgb565(brg655_color):
    """
    Convert BRG655 color to RGB565 format (reverse conversion)
    
    Args:
        brg655_color (int): 16-bit BRG655 color value
    
    Returns:
        int: 16-bit RGB565 color value
    """
    # Extract individual color components from BRG655
    blue = (brg655_color >> 11) & 0x1F   # Upper 5 bits
    red_6bit = (brg655_color >> 5) & 0x3F # Middle 6 bits
    green_5bit = brg655_color & 0x1F     # Lower 5 bits
    
    # Scale red from 6 bits back to 5 bits
    red = red_6bit >> 1
    
    # Scale green from 5 bits back to 6 bits
    green = (green_5bit << 1) | (green_5bit >> 4)  # Duplicate MSB to fill 6th bit
    
    # Reconstruct as RGB565: Red(5) Green(6) Blue(5)
    rgb565_color = (red << 11) | (green << 5) | blue
    
    return rgb565_color

def rgb565_to_rgb888(rgb565_color):
    """
    Convert RGB565 to standard RGB888 for display purposes
    
    Args:
        rgb565_color (int): 16-bit RGB565 color value
    
    Returns:
        tuple: (red, green, blue) values in 0-255 range
    """
    red = (rgb565_color >> 11) & 0x1F
    green = (rgb565_color >> 5) & 0x3F
    blue = rgb565_color & 0x1F
    
    # Scale to 8-bit values
    red = (red * 255) // 31
    green = (green * 255) // 63
    blue = (blue * 255) // 31
    
    return (red, green, blue)

def brg655_to_rgb888(brg655_color):
    """
    Convert BRG655 to standard RGB888 for display purposes
    
    Args:
        brg655_color (int): 16-bit BRG655 color value
    
    Returns:
        tuple: (red, green, blue) values in 0-255 range
    """
    blue = (brg655_color >> 11) & 0x1F
    red = (brg655_color >> 5) & 0x3F
    green = brg655_color & 0x1F
    
    # Scale to 8-bit values
    red = (red * 255) // 63
    green = (green * 255) // 31
    blue = (blue * 255) // 31
    
    return (red, green, blue)

def format_color_info(color_value, format_name):
    """
    Format color information for display
    
    Args:
        color_value (int): 16-bit color value
        format_name (str): Name of the color format
    
    Returns:
        str: Formatted color information
    """
    if format_name == "RGB565":
        rgb888 = rgb565_to_rgb888(color_value)
    else:  # BRG655
        rgb888 = brg655_to_rgb888(color_value)
    
    binary = format(color_value, '016b')
    
    return f"{format_name}: 0x{color_value:04X} | Binary: {binary} | RGB888: {rgb888}"

def main():
    """Main function with examples and interactive mode"""
    print("RGB565 ↔ BRG655 Color Converter")
    print("=" * 40)
    
    # Example conversions
    print("\nExample conversions:")
    
    test_colors = [
        ("Pure Red", 0xF800),
        ("Pure Green", 0x07E0),
        ("Pure Blue", 0x001F),
        ("White", 0xFFFF),
        ("Black", 0x0000),
        ("Yellow", 0xFFE0),
        ("Cyan", 0x07FF),
        ("Magenta", 0xF81F),
    ]
    
    for name, rgb565 in test_colors:
        brg655 = rgb565_to_brg655(rgb565)
        print(f"\n{name}:")
        print(f"  {format_color_info(rgb565, 'RGB565')}")
        print(f"  {format_color_info(brg655, 'BRG655')}")
    
    # Interactive mode
    print("\n" + "=" * 40)
    print("Interactive Mode (press Enter with no input to exit)")
    
    while True:
        try:
            user_input = input("\nEnter RGB565 color (hex, e.g., 0xF800 or F800): ").strip()
            
            if not user_input:
                break
                
            # Parse input (handle with or without 0x prefix)
            if user_input.lower().startswith('0x'):
                color_value = int(user_input, 16)
            else:
                color_value = int(user_input, 16)
            
            # Validate 16-bit range
            if color_value < 0 or color_value > 0xFFFF:
                print("Error: Color value must be between 0x0000 and 0xFFFF")
                continue
            
            # Perform conversion
            brg655 = rgb565_to_brg655(color_value)
            
            print(f"\nConversion Result:")
            print(f"  Input:  {format_color_info(color_value, 'RGB565')}")
            print(f"  Output: {format_color_info(brg655, 'BRG655')}")
            
            # Verify round-trip conversion
            back_to_rgb = brg655_to_rgb565(brg655)
            if back_to_rgb == color_value:
                print(f"  ✓ Round-trip conversion successful")
            else:
                print(f"  ✗ Round-trip conversion failed!")
                
        except ValueError:
            print("Error: Please enter a valid hexadecimal number")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
    
    print("Goodbye!")

def batch_convert(rgb565_list):
    """
    Convert a list of RGB565 colors to BRG655
    
    Args:
        rgb565_list (list): List of RGB565 color values
    
    Returns:
        list: List of corresponding BRG655 color values
    """
    return [rgb565_to_brg655(color) for color in rgb565_list]

# Example usage as a module
if __name__ == "__main__":
    main()
else:
    # When imported as a module, provide a simple example
    print("RGB565 to BRG565 converter module loaded")
    print("Available functions: rgb565_to_brg565(), brg565_to_rgb565(), batch_convert()")