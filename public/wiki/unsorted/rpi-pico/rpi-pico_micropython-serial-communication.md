# Serial Communication with MicroPython on Raspberry Pi Pico

## 1. Flash MicroPython to Your Pico

1. **Download MicroPython**: Get the latest `.uf2` file from [micropython.org](https://micropython.org/download/RPI_PICO/)
2. **Enter BOOTSEL mode**: Hold the BOOTSEL button while plugging in your Pico
3. **Flash firmware**: Drag the `.uf2` file to the Pico drive that appears
4. **Pico reboots automatically** and is ready for MicroPython

## 2. Connect to the Pico's Serial Interface

The Pico will appear as a serial device. Find the port:
- **Windows**: Check Device Manager for a COM port (like COM3, COM4)
- **Linux**: Usually `/dev/ttyACM0`
- **macOS**: Usually `/dev/tty.usbmodem*`

## 3. MicroPython Code on the Pico

Create a `main.py` file on your Pico:

```python
import sys
import select
import time

print("Pico ready for serial communication!")

while True:
    # Check if data is available from computer
    if select.select([sys.stdin], [], [], 0)[0]:
        try:
            received_data = input().strip()
            print(f"Received: {received_data}")
            
            # Echo back or process the data
            if received_data == "ping":
                print("pong")
            elif received_data == "led":
                print("LED toggled!")
            else:
                print(f"Echo: {received_data}")
                
        except EOFError:
            pass
    
    # Send periodic data (optional)
    # print("Heartbeat from Pico")
    time.sleep(0.1)  # Small delay to prevent overwhelming
```

## 4. Python Script on Your Computer

```python
import serial
import time
import threading

# Adjust the port for your system
PORT = '/dev/ttyACM0'  # Linux/macOS
# PORT = 'COM3'        # Windows - check Device Manager

try:
    ser = serial.Serial(PORT, 115200, timeout=1)
    print(f"Connected to Pico on {PORT}")
    time.sleep(2)  # Give Pico time to boot
    
    def read_from_pico():
        """Continuously read from Pico"""
        while True:
            if ser.in_waiting > 0:
                try:
                    data = ser.readline().decode('utf-8').strip()
                    if data:
                        print(f"Pico: {data}")
                except UnicodeDecodeError:
                    pass
            time.sleep(0.1)
    
    # Start reading thread
    read_thread = threading.Thread(target=read_from_pico, daemon=True)
    read_thread.start()
    
    # Main loop - send commands
    while True:
        user_input = input("Enter command (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        
        ser.write(f"{user_input}\n".encode('utf-8'))
        time.sleep(0.1)

except serial.SerialException as e:
    print(f"Serial error: {e}")
    print("Make sure the Pico is connected and the port is correct")
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    if 'ser' in locals():
        ser.close()
```

## 5. Alternative: Simple Interactive Testing

You can also test immediately using a terminal program:

```bash
# Linux/macOS
screen /dev/ttyACM0 115200
# Press Ctrl+A, then K to exit

# Or use picocom
picocom /dev/ttyACM0 -b 115200
# Press Ctrl+A, Ctrl+X to exit
```

## 6. Installing Required Python Libraries

On your computer, install pyserial:
```bash
pip install pyserial
```

## Tips

- The Pico's serial connection is automatically configured at 115200 baud
- Use `print()` on the Pico to send data to your computer
- Use `input()` on the Pico to receive data from your computer
- Remember that `input()` is blocking, so use `select.select()` for non-blocking reads
- You can edit files directly on the Pico using a MicroPython IDE like Thonny

Try the basic setup first, then let me know if you want to add specific functionality like sensor readings, LED control, or other features!