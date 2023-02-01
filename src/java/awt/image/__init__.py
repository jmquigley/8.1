

__all__ = ["BufferedImage"]

from typing import Any

from java.awt import Image


class BufferedImage(Image):
    def __init__(self, *args):
        # type: (*Any) -> None
        print(args)
