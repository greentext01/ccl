import json
from pathlib import Path
from zipfile import ZipFile


def package(bundled, assets: list[Path]):
    with ZipFile("project.sb3", "w") as zf:
        zf.writestr("project.json", json.dumps(bundled))
        for asset in assets:
            zf.writestr(asset.name, asset.read_text())
