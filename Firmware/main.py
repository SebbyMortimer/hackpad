# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.rgb import RGB

import displayio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
import terminalio

# initialize I2C for display (adjust pins if different)
i2c = board.I2C()

# release any displays that might be in use
displayio.release_displays()
oled_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

WIDTH = 128
HEIGHT = 64
display = adafruit_displayio_ssd1306.SSD1306(oled_bus, width=WIDTH, height=HEIGHT)

# show basic text
splash = displayio.Group()
text = "Hi!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=0, y=10)
splash.append(text_area)
display.show(splash)

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

leds = RGB(pixel_pin=board.GP26, num_pixels=2)
keyboard.extensions.append(leds)

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.GP3, board.GP4, board.GP2, board.GP1]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [
        KC.MACRO(Press(KC.LCTRL), Tap(KC.S), Release(KC.LCTRL)),
        KC.MACRO("https://sebbymortimer.co.uk", Tap(KC.ENTER)),
        KC.MACRO(Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL)),
        KC.MACRO(Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL)),
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()