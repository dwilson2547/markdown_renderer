# Raspberry Pi Pico

Pico Documentation: https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html

Zadig: https://zadig.akeo.ie/

Getting started guide: https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf

1.14 in display: https://www.waveshare.com/pico-lcd-1.14.htm

display colors are in rgb565 format, or should i say brg565. standard rgb5465 is a hex representation of 16 bits defining a color. The first 5 bits represent the red value, the next 6 bits represent the green value, and the last 5 bits represent the blue value. This display seems to use this standard, but the colors are in the wrong order. For this display, the first 5 bits are blue, the next 6 bits are red, and teh last 5 bits are green. If you're using a color chart online and need to convert between the default and this weird standard, you can do the following. For the record, I didn't recognize this color standard and used claude ai to figure it out. it became 

new_red = old_blue<br>
new_green = old_red * 2<br>
new_blue = old_green / 2

Standard

| Red | Green | Blue | 
| -- | -- | -- |
| 00000 | 000000 | 00000 |
| 11111 | 111111 | 11111 |

Waveshare 1.14" display

| Blue | Red | Green | 
| -- | -- | -- |
| 00000 | 000000 | 00000 |
| 11111 | 111111 | 11111 |

Getting started with micropython
find executable online, connect pico to pc while holding down bootselect button, copy executable to pico
open vscode
install pico libraries
create new pico micropython project


getting script to autorun

https://forums.raspberrypi.com/viewtopic.php?f=144&t=300539#p1805666
See Page 113 in Chapter 9 of the Get Started with Micropython 'book'.

rename script to main.py, in vscode hit control shift p -> MicroPico: Upload current file to pico

debugging: 

vscode control shift p -> MicroPico: Run current file on pico


python print and std.in interface are serial by default, baud rate is 115200
