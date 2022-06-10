from caracal.core.sprite import Sprite
from caracal.core.register_sprite import register_sprite

class Stage(Sprite):
    is_stage = True

register_sprite(Stage)
