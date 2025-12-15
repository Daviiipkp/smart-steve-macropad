import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledReactionType, OledData
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.row_pins = (board.D4, board.D5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]
keyboard.extensions.append(MediaKeys())

rgb = RGB(pixel_pin=board.D6, num_pixels=1, hue_default=100, val_default=100)
keyboard.extensions.append(rgb)

oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["Layer"]},
        corner_two={0:OledReactionType.LAYER,1:["1","2"]},
        corner_three={0:OledReactionType.STATIC,1:["Smart"]},
        corner_four={0:OledReactionType.STATIC,1:["Steve"]}
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False,
)
keyboard.extensions.append(oled_ext)

keyboard.keymap = [
    [

        KC.A,    KC.B,    KC.C,    KC.D,
        KC.E,    KC.F,    KC.G,    KC.H,
    ]
]

encoder_handler.pins = ((board.D9, board.D10, None, False),) 
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE),),
]

if __name__ == '__main__':
    keyboard.go()