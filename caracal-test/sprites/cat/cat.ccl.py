from caracal.core.sprite import Sprite
from caracal.blocks.looks.say import say
from caracal.core.register_sprite import register_sprite

class Cat(Sprite):
    position = (200, 200)
    
    def on_flag_clicked(self):
        say("Hello world!")

    def on_flag_clicked(self):
        say("Hello world!")
 
register_sprite(Cat)
