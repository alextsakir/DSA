from random import choice, randint
from typing import NoReturn, Final, Optional, Iterable

_CODE = str
SIZE: int = 20

_8: int = 987_654_321 // 123_456_789

class Generator:
    _LETTERS: list[str] = [chr(position) for position in range(65, 91)]  # - get latin capital letters from ascii chart
    _HEX_LETTERS: list[str] = [chr(position) for position in range(65, 70)]  # ------- letters used in hex: A B C D E F

    SAMPLE: list[_CODE] = ["WELC-OMET-OTHE", "IEEE-XTRE-ME14", "AAAA-0000-A0A0",
                           "AAAA-0000-A0A1", "AAAA-0000-A0AB", "AAAA-0000-ABAB"]

    def __init__(self, only_hex: Optional[bool] = False) -> NoReturn:
        self.only_hex: bool = only_hex if only_hex else False
        return

    @staticmethod
    def load(file_name: str) -> list[_CODE]:
        return open(file_name, "r").readlines()  # ------------------------------------------- load pre-generated codes

    def _code(self) -> list[str, str, str]:  # -------------- protected method generating a list of three code segments
        characters = Generator._HEX_LETTERS if self.only_hex else Generator._LETTERS
        out: list = [str().join([choice(characters) for _ in range(4)]),
                     str().join([str(randint(0, 9)) for _ in range(4)])]
        return out + [str().join([choice(characters) for _ in range(4)])]

    def code(self) -> _CODE:
        """ Method that returns a 12-character code without readability dashes. """
        return str().join(self._code())

    def dash(self) -> _CODE:
        """ Method that returns a 12-character code with readability dashes. """
        return str("-").join(self._code())

    @staticmethod
    def alter(code: _CODE) -> _CODE:
        """ Method that removes dashes if they exist or adds them if they don't. """
        assert len(code) in (12, 14)
        if len(code) == 12:
            code = code[:4] + "-" + code[4:8] + "-" + code[8:]
        elif len(code) == 14:
            code = code.replace("-", str())
        return code

    def __call__(self, amount: int) -> list[_CODE]:
        return [self.code() for _ in range(amount)]


class Hamming:

    @staticmethod
    def distance(left: _CODE, right: _CODE) -> int:
        counter: int = 0
        for index in range(len(left)):
            if left[index] != right[index]: counter += 1
        return counter

    @staticmethod
    def smart_distance(left: _CODE, right: _CODE) -> int:
        return sum([left_char != right_char for left_char, right_char in zip(left, right)])

    @staticmethod
    def one(left: _CODE, right: _CODE) -> bool:
        assert not len(left) - len(right)
        flag: bool = False
        for left_char, right_char in zip(left, right):
            if left_char != right_char:
                if flag:
                    return False
                else:
                    flag = True
        return True

    def test(self, data: list[_CODE]):
        for left_index, left in enumerate(data):
            for right_index, right in enumerate(data):
                if left_index == right_index: continue
                print(f"DISTANCE OF {left} AND {right}:\t {self.distance(left, right)}")
            print()


class Codes:

    class _Table:

        def __init__(self, size: int) -> NoReturn:
            self._store: list[list[_CODE]] = list([] for _ in range(size))
            return

        def __iter__(self) -> Iterable: return iter(self._store)

        def __getitem__(self, item): return self._store[item]

    def __init__(self, size: int) -> NoReturn:
        self.data: Final[list[_CODE]] = generator(size)
        self.table: Codes._Table = Codes._Table(size)
        return

    def __str__(self) -> str: return str(self.data)

    def __len__(self) -> int: return len(self.data)

    @staticmethod
    def hash(code: _CODE) -> int: return sum(ord(char) for char in code) % SIZE

    def analysis(self) -> str:
        out: str = "Table Analysis\n"
        for list_index, code_list in enumerate(self.table):
            out += f"List of index {list_index} with {len(code_list)} elements\n"
        out += f"Total codes: {len(self)}, codes added in table: {self.table_counter}\t\t"
        out += "CORRECT" if len(self) == self.table_counter else "WRONG"
        return out + "\n"

    def table_init(self) -> NoReturn:
        for code in self.data:
            self.table[Codes.hash(code)].insert(0, code)
        return

    @property
    def table_counter(self) -> int: return sum(len(code_list) for code_list in self.table)


if __name__ == "__main__":
    generator = Generator(only_hex=True)
    hamming = Hamming()
    codes = Codes(SIZE)
    print(codes)
    codes.table_init()
    print(codes.analysis())
