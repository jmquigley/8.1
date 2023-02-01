

__all__ = ["SimplifiedTagPath"]

from com.inductiveautomation.ignition.common.tags.model import TagPath
from com.inductiveautomation.ignition.common.tags.paths import AbstractTagPath


class SimplifiedTagPath(AbstractTagPath):
    def __init__(self, delegate):
        # type: (TagPath) -> None
        print(delegate)
