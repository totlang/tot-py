from io import TextIOWrapper
from typing import Union
from queue import LifoQueue
from enum import Enum

# The max depth the deserializer will try to parse before raising an Exception
DEFAULT_STACK_SIZE: int = 1024


class State(Enum):
    """
    The thing the deserializer is currently parsing.
    """
    DICT = 0
    LIST = 1
    STRING = 2
    VALUE = 3
    WS = 4


class BaseDeserializer(object):
    input: Union[list, TextIOWrapper] = None
    output: dict = {}
    stack: LifoQueue = None

    def __init__(self, stack_size: int) -> None:
        self.stack = LifoQueue(stack_size)
        self._deserialize()

    def _peek(self) -> Union[str, None]:
        """
        Get the next input character without consuming it.
        """
        raise NotImplementedError("BaseDeserializer._peek")

    def _take(self) -> Union[str, None]:
        """
        Get the next input character and consume it.
        """
        raise NotImplementedError("BaseDeserializer._take")

    def _deserialize(self) -> None:
        next_char: Union[str, None] = self._peek()
        while next_char != None:
            if next_char == "\"":
                pass
            elif next_char == "{":
                pass
            elif next_char == "[":
                pass
            else:
                pass

    def _parse_key(self) -> None:
        pass

    def _parse_boolean(self) -> None:
        pass

    def _parse_number(self) -> None:
        pass

    def _parse_string(self) -> None:
        pass

    def _parse_list(self) -> None:
        pass

    def _parse_dict(self) -> None:
        pass


class TextDeserializer(BaseDeserializer):
    def __init__(self, text: str, stack_size: int = DEFAULT_STACK_SIZE) -> None:
        self.input: list = list(text)
        self.input.reverse()

        super().__init__(stack_size)

    def _peek(self) -> Union[str, None]:
        return self.input[-1] if len(self.input) > 0 else None

    def _take(self) -> Union[str, None]:
        return self.input.pop() if len(self.input) > 0 else None


class FileDeserializer(BaseDeserializer):
    def __init__(self, path: str, encoding: str = "utf-8", stack_size: int = DEFAULT_STACK_SIZE) -> None:
        self.input: TextIOWrapper = open(path, encoding=encoding)

        super().__init__()

    def _peek(self) -> Union[str, None]:
        c = self.input.read(1)
        self.input.seek(-1)
        return c

    def _take(self) -> Union[str, None]:
        return self.input.read(1)


class DeserializeError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
