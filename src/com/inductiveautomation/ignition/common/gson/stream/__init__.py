

from typing import Any

from enum import Enum

from java.io import Closeable, Flushable, Reader, Writer
from java.lang import Object, String


class JsonReader(Object, Closeable):
    def __init__(self, in_):
        # type: (Reader) -> None
        print(in_)

    def beginArray(self):
        # type: () -> None
        pass

    def beginObject(self):
        # type: () -> None
        pass

    def close(self):
        # type: () -> None
        pass

    def endArray(self):
        # type: () -> None
        pass

    def endObject(self):
        # type: () -> None
        pass

    def getPath(self):
        # type: () -> String
        pass

    def hasNext(self):
        # type: () -> bool
        return True

    def isLenient(self):
        # type: () -> bool
        return True

    def nextBoolean(self):
        # type: () -> bool
        return True

    def nextDouble(self):
        # type: () -> float
        pass

    def nextInt(self):
        # type: () -> int
        pass

    def nextLong(self):
        # type: () -> long
        pass

    def nextName(self):
        # type: () -> String
        pass

    def nextNull(self):
        # type: () -> None
        pass

    def nextString(self):
        # type: () -> String
        pass

    def peek(self):
        # type: () -> JsonToken
        pass

    def setLenient(self, lenient):
        # type: (bool) -> None
        pass

    def skipValue(self):
        # type: () -> None
        pass


class JsonToken(Enum):
    BEGIN_ARRAY = None  # type: JsonToken
    BEGIN_OBJECT = None  # type: JsonToken
    BOOLEAN = None  # type: JsonToken
    END_ARRAY = None  # type: JsonToken
    END_DOCUMENT = None  # type: JsonToken
    END_OBJECT = None  # type: JsonToken
    NAME = None  # type: JsonToken
    NULL = None  # type: JsonToken
    NUMBER = None  # type: JsonToken
    STRING = None  # type: JsonToken


class JsonWriter(Object, Closeable, Flushable):
    def __init__(self, out):
        # type: (Writer) -> None
        print(out)

    def beginArray(self):
        # type: () -> JsonWriter
        pass

    def beginObject(self):
        # type: () -> JsonWriter
        pass

    def close(self):
        # type: () -> None
        pass

    def endArray(self):
        # type: () -> JsonWriter
        pass

    def endObject(self):
        # type: () -> JsonWriter
        pass

    def flush(self):
        # type: () -> None
        pass

    def getSerializeNulls(self):
        # type: () -> bool
        return True

    def isHtmlSafe(self):
        # type: () -> bool
        return True

    def isLenient(self):
        # type: () -> bool
        return True

    def jsonValue(self, value):
        # type: (String) -> JsonWriter
        pass

    def name(self, name):
        # type: (String) -> JsonWriter
        pass

    def setHtmlSafe(self, htmlSafe):
        # type: (bool) -> None
        pass

    def setIndent(self, indent):
        # type: (String) -> None
        pass

    def setLenient(self, lenient):
        # type: (bool) -> None
        pass

    def setSerializeNulls(self, serializeNulls):
        # type: (bool) -> None
        pass

    def value(self, arg):
        # type: (Any) -> JsonWriter
        pass
