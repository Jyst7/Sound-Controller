import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

# Modules/extensions
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.rgb import RGB

# Create keyboard
keyboard = KMKKeyboard()

# ------------------
# BUTTONS (matrix) 
# ------------------
keyboard.col_pins = (board.GP17, board.GP19, board.GP20)
keyboard.row_pins = (board.GP16,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ------------------
# ENCODERS
# ------------------
encoder_handler = EncoderHandler()
keyboard.modules.append(Layers())
keyboard.modules.append(encoder_handler)
keyboard.modules.append(MediaKeys())
keyboard.modules.append(MouseKeys())


encoder_handler.pins = (
    (board.GP27, board.GP26, None),
    (board.GP25, board.GP24, None),
    (board.GP22, board.GP21, None),
)

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),
    ((KC.MW_UP, KC.MW_DN),),
    ((KC.RGB_VAD, KC.RGB_VAI),),
]

# ------------------
# NEOPIXELS (RGB extension)
# ------------------
NUM_PIXELS_DEFAULT = 8

rgb1 = RGB(pixel_pin=board.GP1, num_pixels=NUM_PIXELS_DEFAULT)
rgb2 = RGB(pixel_pin=board.GP2, num_pixels=NUM_PIXELS_DEFAULT)
rgb3 = RGB(pixel_pin=board.GP4, num_pixels=NUM_PIXELS_DEFAULT)

keyboard.extensions.append(rgb1)
keyboard.extensions.append(rgb2)
keyboard.extensions.append(rgb3)

# ------------------
# KEYMAP
# ------------------
TRANS = KC.TRNS

keyboard.keymap = [
    [
        # Layer 0: single row with 3 keys
        KC.A,    # col GP17
        KC.B,    # col GP19
        KC.C,    # col GP20
    ],
]

# ------------------
# Tweakables / Debug
# ------------------
keyboard.debug_enabled = True

if __name__ == '__main__':
    keyboard.go()
