from caracal.core.sprite import Sprite
from caracal.blocks.looks.say import say
from caracal.core.register_sprite import register_sprite

class Cat(Sprite):
    def on_flag_clicked(self):
        say("hi mom")

    def on_flag_clicked(self):
        say("hi mom")

register_sprite(Cat)
