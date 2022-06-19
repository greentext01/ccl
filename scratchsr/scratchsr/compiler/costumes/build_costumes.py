import hashlib
from scratchsr.compiler.costumes.iterate_costumes import iterate_costumes

COSTUME_EXTENSIONS = [
    ".svg",
    ".png",
    ".bmp",
    ".jpg",
    ".jpeg",
    ".gif",
]


def build_assets(sprite):
    out = []
    files = []

    for asset in iterate_costumes(sprite):
        files.append(asset)
        hash = hashlib.md5(asset.read_bytes()).hexdigest()
        out.append({
            "assetId": hash,
            "name": asset.stem,
            "bitmapResolution": 1,
            "md5ext": hash + asset.suffix,
            "dataFormat": asset.suffix.lstrip("."),
            # TODO: Add support for changing rotation center (costumes.json file maybe?)
            "rotationCenterX": 0,
            "rotationCenterY": 0
        })
                
    return out, files
