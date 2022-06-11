import hashlib
import os
from pathlib import Path

from scratchsr.errors.missing_assets_error import MissingAssetsError

COSTUME_EXTENSIONS = [
    ".svg",
    ".png",
    ".bmp",
    ".jpg",
    ".jpeg",
    ".gif",
]


def build_assets(sprite):
    sprite_dir = Path(sprite.__module__).parent
    sprite_path = sprite_dir.relative_to(Path.cwd() / ".cclfiles")
    asset_path = sprite_path / "assets"

    if not asset_path.exists() and sprite.is_stage:
        raise MissingAssetsError(sprite_path.absolute())
    elif not asset_path.exists():
        return {}

    out = []
    files = []

    for asset in asset_path.glob("**/*"):
        if asset.is_file():
            hash = hashlib.md5(asset.read_bytes()).hexdigest()
            if asset.suffix in COSTUME_EXTENSIONS:
                files.append(asset)
                out.append({
                    "assetId": hash,
                    "name": os.path.splitext(asset.name)[0],
                    "bitmapResolution": 1,
                    "md5ext": hash + asset.suffix,
                    "dataFormat": asset.suffix.lstrip("."),
                    # TODO: Add support for changing rotation center (costumes.json file maybe?)
                    "rotationCenterX": 40,
                    "rotationCenterY": 50
                })
                
    return out, files
