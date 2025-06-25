import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.rgb import RGB
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)
keyboard.row_pins = ()  # Direct pins (1D scan)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

rgb = RGB(pixel_pin=board.GP8, num_pixels=2, rgb_order=(0, 1, 2))  # Adjust num_pixels as needed
keyboard.modules.append(rgb)

keyboard.keymap = [
    [
        KC.LGUI(KC.C), KC.LGUI(KC.V), KC.W, KC.LSFT,
        KC.SPACE, KC.A, KC.S, KC.D,
    ]
]

if __name__ == '__main__':
    keyboard.go()
