from enum import Enum
from typing import List

class __MyEnumeration(Enum):  # ------------------------------------------------------------------------- Enum Template

    @classmethod
    def length(cls) -> int: return len(cls.members())

    @classmethod
    def members(cls) -> List["__MyEnumeration"]: return list([element for element in cls])

    @classmethod
    def display(cls) -> str: return str(list([str(element) for element in cls]))

class UserTypes(__MyEnumeration): USER, DOCTOR, ADMIN, OTHER = "USER", "DOCTOR", "ADMIN", "OTHER"  # -------- UserTypes

class Sexes(__MyEnumeration): MAN, WOMAN, OTHER = "MAN", "WOMAN", "OTHER"  # ------------------------------------ Sexes

class QuestionTypes(__MyEnumeration): MULTIPLE_CHOICE, OPEN_ENDED = "MULTIPLE_CHOICE", "OPEN_ENDED"  # -- QuestionTypes


__enumerations: list[type(__MyEnumeration)] = [UserTypes, Sexes, QuestionTypes]

def display() -> str:
    out: str = "Enumerations Module\n"
    for cls in __enumerations:
        out += cls.__name__ + "\t" + str(cls.length()) + "\t" + cls.display() + "\n"  # ------------------- duck typing
    return out


__all__: List[str] = [cls.__name__ for cls in __enumerations]

if __name__ == "__main__": print(display())
