import hashlib
from scratchsr.compiler.costumes.get_asset_path import get_asset_path

COSTUME_EXTENSIONS = [
    ".svg",
    ".png",
    ".bmp",
    ".jpg",
    ".jpeg",
    ".gif",
]

def iterate_costumes(sprite):
    asset_path = get_asset_path(sprite)

    for asset in asset_path.glob("**/*"):
        if asset.is_file():
            if asset.suffix in COSTUME_EXTENSIONS:
                yield asset
