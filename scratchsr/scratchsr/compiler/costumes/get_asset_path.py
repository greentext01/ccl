from pathlib import Path
from scratchsr.user.sprite import Sprite
from scratchsr.errors.missing_assets_error import MissingAssetsError


def get_asset_path(sprite, error=False):
    if hasattr(sprite, "__module__"):
        sprite_dir = Path(sprite.__module__).parent
    elif type(sprite) == str:
        sprite_dir = Path(sprite).parent
    else:
        raise ValueError("sprite must have a __module__ attribute or be a string")
    
    sprite_path = sprite_dir.relative_to(Path.cwd() / ".scsrfiles")
    asset_path = sprite_path / "assets"

    if not asset_path.exists() or not asset_path.is_dir():
        if error or sprite.is_stage:
            raise MissingAssetsError(sprite_path.absolute())
    else:
        return asset_path
