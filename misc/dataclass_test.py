from dataclasses import dataclass

@dataclass
class Data:
    left: int
    right: int
    summation: int


first: Data = Data(2, 7, 5)
print(repr(first), first.summation)
