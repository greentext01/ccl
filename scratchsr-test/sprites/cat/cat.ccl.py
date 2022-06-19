from scratchsr.user.sprite import Sprite
from scratchsr.blocks.motion import go_to, RANDOM
from scratchsr.user.register_sprite import register_sprite
from scratchsr.user.find_costume import find_costume

class Cat(Sprite):
    position = (200, 200)
    size = 25
    start_costume = find_costume("cat")
    
    def on_flag_clicked(self):
        var = 1
        go_to(RANDOM)
 
register_sprite(Cat)
