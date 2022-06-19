from scratchsr.user.sprite import Sprite
from scratchsr.user.register_sprite import register_sprite

class Stage(Sprite):
    is_stage = True

register_sprite(Stage)
