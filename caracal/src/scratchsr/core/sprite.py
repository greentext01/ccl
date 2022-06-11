from xmlrpc.client import boolean
from .costume import Costume


class Sprite:
    position: tuple[int, int] = (0, 0)
    costumes: list[Costume] = []
    start_costume: int = 0
    volume: int = 100
    start_layer: int = 0
    tempo: int = 60
    video_transparency: int = 50
    video_state: str = "on"
    is_stage: boolean = False
    sounds: list[dict] = []
    text_to_speech_language: str = "English"
    size: int = 100

    def ccl__build(self):
        pass
