__all__ = [
    "TagManager",
    "TagPath"
]

from typing import Union

from com.inductiveautomation.ignition.common import Path
from com.inductiveautomation.ignition.common.config import Property
from java.lang import String


class TagManager(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TagManager, cls).__new__(cls)

        return cls._instance

    def browseAsync(self, tagPath, browseFilter):
        pass

    def readAsync(self, tagPaths):
        pass

    def subscribeAsync(self, tagPath, listener):
        pass

    def unsubscribeAsync(self, tagPath, listener):
        pass


class TagPath(Path):
    def compareTo(self, that):
        # type: (TagPath) -> int
        pass

    def getChildPath(self, arg):
        # type: (Union[Property, String]) -> TagPath
        pass

    def getItemName(self):
        # type: () -> String
        pass

    def getLastPathComponent(self):
        # type: () -> String
        pass

    def getParentPath(self):
        # type: () -> Path
        pass

    def getPathComponent(self, i):
        # type: (int) -> String
        pass

    def getPathLength(self):
        # type: () -> int
        pass

    def getProperty(self):
        # type: () -> Property
        pass

    def getSource(self):
        # type: () -> String
        pass

    def isAncestorOf(self, path):
        # type: (Path) -> bool
        return True

    def toStringFull(self):
        # type: () -> String
        pass

    def toStringPartial(self):
        # type: () -> String
        pass
