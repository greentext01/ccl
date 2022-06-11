import hashlib
import json
from pathlib import Path
from zipfile import ZipFile


def package(bundled, assets: list[Path]):
    with ZipFile("project.sb3", "w") as zf:
        zf.writestr("project.json", json.dumps(bundled, indent=2))
        for asset in assets:
            zf.writestr(hashlib.md5(asset.read_bytes()).hexdigest() +
                        asset.suffix, asset.read_bytes())
