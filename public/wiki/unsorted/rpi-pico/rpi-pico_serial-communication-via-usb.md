# Raspberry Pi Pico Serial Communication via USB

For serial communication over USB between your Raspberry Pi Pico and computer, you have several options:

## MicroPython (Easiest)

MicroPython automatically sets up USB serial communication:

1. **Flash MicroPython** to your Pico (download `.uf2` from raspberrypi.org)
2. **Connect via serial terminal** on your computer:
   - **Windows**: Use PuTTY, Tera Term, or Windows Terminal
   - **macOS/Linux**: Use `screen`, `minicom`, or `picocom`

```bash
# Linux/macOS examples
screen /dev/ttyACM0 115200
# or
picocom /dev/ttyACM0 -b 115200

# Windows (check Device Manager for COM port)
# Use PuTTY with COM3, COM4, etc. at 115200 baud
```

3. **Python code on Pico**:

```python
import sys
import time

while True:
    # Read from computer
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = input()
        print(f"Received: {line}")
    
    # Send to computer
    print("Hello from Pico!")
    time.sleep(1)
```

## CircuitPython

Similar to MicroPython but with slightly different syntax:

```python
import supervisor
import time

while True:
    if supervisor.runtime.serial_bytes_available:
        data = input()
        print(f"Got: {data}")
    
    print("CircuitPython here!")
    time.sleep(1)
```

## C/C++ with Pico SDK

For more control and performance:

```c
#include <stdio.h>
#include "pico/stdlib.h"

int main() {
    stdio_init_all();
    
    printf("Pico serial ready!\n");
    
    while (true) {
        char input = getchar_timeout_us(0);
        if (input != PICO_ERROR_TIMEOUT) {
            printf("You typed: %c\n", input);
        }
        
        printf("Hello from C!\n");
        sleep_ms(1000);
    }
    
    return 0;
}
```

## Python Script on Computer

To communicate from your computer:

```python
import serial
import time

# Adjust port name for your system
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)  # Linux/macOS
# ser = serial.Serial('COM3', 115200, timeout=1)        # Windows

while True:
    # Send data to Pico
    ser.write(b"Hello Pico!\n")
    
    # Read response from Pico
    if ser.in_waiting > 0:
        response = ser.readline().decode('utf-8').strip()
        print(f"Pico says: {response}")
    
    time.sleep(1)
```

## Finding the Serial Port

- **Windows**: Check Device Manager → Ports (COM & LPT)
- **Linux**: Usually `/dev/ttyACM0` or `/dev/ttyUSB0`
- **macOS**: Usually `/dev/cu.usbmodem*` or `/dev/tty.usbmodem*`

The MicroPython approach is usually the quickest to get started with. Which method would you prefer to use?