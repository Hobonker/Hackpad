from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.rgb import RGB
import board

keyboard = KMKKeyboard()

layers = Layers()
keyboard.modules.append(layers)

keyboard.row_pins = (
    board.GP0,  # sw5 -> SPACE
    board.GP3,  # sw4 -> A
    board.GP4,  # sw3 -> S
    board.GP2,  # sw2 -> W
    board.GP1,  # sw1 -> D
)

keyboard.col_pins = ()
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.SPACE, KC.A, KC.S, KC.W, KC.D],
]

rgb = RGB(pixel_pin=board.GP6, num_pixels=2, val_limit=100, hue_default=100)
rgb.effect = "rainbow"  # Optional: 'solid_color', 'breath', etc.
keyboard.extensions.append(rgb)

if __name__ == '__main__':
    keyboard.go()
