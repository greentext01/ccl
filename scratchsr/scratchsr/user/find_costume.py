import inspect
from scratchsr.compiler.costumes.iterate_costumes import iterate_costumes
from scratchsr.user.sprite import Sprite
from scratchsr.compiler.costumes.get_asset_path import get_asset_path

def find_costume(costume_name):
    """
    Finds the costume with the given name.
    """
    sprite_path = inspect.stack()[1].filename

    for i, file in enumerate(iterate_costumes(sprite_path)):
        if file.stem == costume_name:
            return i
