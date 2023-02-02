__all__ = [
    "TagStructureEvent",
    "TagStructureListener"
]

class TagStructureEvent(object):
    def getAddedTags():
        return []
        
    def getMovedTags():
        return []
        
    def getRemovedTagsInfo():
        return []


class TagStructureListener(object):
    	def tagStructureChanged(event):
            pass