from ..util import registry

def register_sprite(sprite):
    registry.registries.get("sprites").append(sprite)
