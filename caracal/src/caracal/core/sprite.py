from .costume import Costume


class Sprite:
    position: tuple[int, int] = 200, 200
    costumes: list[Costume]
    start_costume: int
    volume: int
    layerOrder: int
    tempo: int
    videoTransparency: int
    videoState: str
    blocks: list[dict]

    def ccl__build(self):
        pass
