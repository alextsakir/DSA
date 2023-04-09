from enum import Enum, unique
from typing import final, TypeVar, NoReturn, Optional, List

_DT = TypeVar("_DT", int, float, str)
"""Specifies supported file types, currently int, float or str. Stands for _DataTypes."""

@final
class Stack:

    """
    Class that implements a stack file structure containing either Integers, Floats or Strings.
    name: string that stores the name of the object
    description: string that stores a brief description
    capacity: integer, the capacity of the stack
    Use graph_print() method to see file stores in the object.
    18 March 2023
    """

    _DEFAULT_CAPACITY: int = 16

    class OverflowException(Exception): pass  # -------------------------------------------------------------- OVERFLOW

    class UnderflowException(Exception): pass  # ------------------------------------------------------------ UNDERFLOW

    # =================================================================================================================

    class Cell:

        def __init__(self, name: str, cls: type) -> NoReturn:
            self.name: str = name
            self.cls: type = cls
            return

    @unique
    class DataType(Enum):

        INTEGER, FLOAT, STRING = ("INTEGER", int), ("FLOAT", float), ("STRING", str)

        @classmethod
        def __members(cls) -> List["Stack.DataType"]: return list([element for element in cls])

        @staticmethod
        def get(data: _DT) -> "Stack.DataType":
            for member in Stack.DataType.__members():
                print()
                if type(data) == member.value: return member
                # if isinstance(file, element.value.cls): return element

    # =================================================================================================================

    class StackElement:

        """
        Inner class used to implement a Stack element. Use type property to see which file type is stored in the
        element. Use has_data or is_empty to check if the element holds a file value.
        """

        __slots__: list[str] = ["data", "__type"]

        def __init__(self, data: _DT) -> NoReturn:
            self.data: _DT = data
            self.__type: Optional[Stack.DataType] = Stack.DataType.get(data)
            assert self.__type is not None
            return

        def __str__(self) -> str: return self.__type.value[0] + " ELEMENT: " + str(self.data)

        def __bool__(self) -> bool: return self.data is not None

        def __eq__(self, other) -> bool: return self.__type == other.__type and self.data == other.file

        def __add__(self, other) -> "Stack.StackElement": return Stack.StackElement(self.data + other.file)

        @property
        def type(self) -> "Stack.DataType": return self.__type

        @property
        def has_data(self) -> bool: return bool(self)

    # =================================================================================================================

    __slots__: list[str] = ["__capacity", "name", "description", "__store"]

    def __init__(self, capacity: int = _DEFAULT_CAPACITY, name: Optional[str] = None,
                 description: Optional[str] = None) -> NoReturn:
        self.__capacity: int = capacity
        self.name: Optional[str] = name
        self.description: Optional[str] = description
        self.__store: List[Stack.StackElement] = list()
        return

    def __str__(self) -> str:
        out: str = "Stack object: "
        if self.name: out += self.name
        if self.description: out += ":\t\t" + self.description
        out += "\n"
        for element in self.__store: out += str(element) + "\n"
        return out

    def __len__(self) -> int: return len(self.__store)

    @property
    def capacity(self) -> int: return self.__capacity

    @property
    def is_empty(self) -> bool: return not len(self)

    @property
    def is_full(self) -> bool: return len(self) == self.capacity

    def clear(self) -> NoReturn: self.__store = list()

    @property
    def peek(self) -> Optional[_DT]: return self.__store[-1].data if not self.is_empty else None

    def peek_type(self) -> Optional[str]:
        if self.is_empty: return None
        return self.__store[-1].type.value

    def push(self, data: _DT) -> bool:
        if not self.is_full:
            self.__store.append(Stack.StackElement(data))
            return True
        raise Stack.OverflowException

    @property
    def pop(self) -> bool:
        if not self.is_empty:
            self.__store.pop(-1)
            return True
        raise Stack.UnderflowException

    def cleanup(self) -> int:
        """
        Method that zips the stored elements depending on their file type. For example, if the Stack elements were:
        [[1], [4], [22.3], ["adc"], [-3], ["def"]], they will get: [[2], [22.3], ["abcdef"]]
        """
        for cls in [int, float, str]:
            backup: List["Stack.StackElement"] = self.__store
            self.clear()
            new_element: "Stack.StackElement" = Stack.StackElement(cls())
            for element in backup:
                if element.type == cls: new_element += element
            self.__store.append(new_element)
        return len(backup) - len(self)


if __name__ == "__main__":
    cell = Stack.DataType.Cell("34", bool)
    print(cell.name, cell.cls, type(cell.cls))

    stack: Stack = Stack(capacity=4, name="My Stack", description="sample stack of integers")
    print(stack)
    print(stack.is_empty)
    # stack.push(2)
