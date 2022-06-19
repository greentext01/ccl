from dataclasses import dataclass


@dataclass
class Costume:
    asset_id: str
    md5ext: str
    format: str
    name: str
    rotation_center_x: int
    rotation_center_y: int
