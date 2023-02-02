__all__ = [
    "GatewayTagManager",
    "TagStructureEvent",
    "TagStructureListener"
]

from com.inductiveautomation.ignition.common.tags.model import TagManager


class GatewayTagManager(TagManager):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GatewayTagManager, cls).__new__(cls)

        return cls._instance

    def addTagStructureListener(self, provider, listener):
        pass

    def removeTagStructureListener(self, provider, listener):
        pass


class TagStructureEvent(object):
    def getAddedTags(self):
        return []

    def getMovedTags(self):
        return []

    def getRemovedTagsInfo(self):
        return []


class TagStructureListener(object):
    def tagStructureChanged(self, event):
        pass
