from random import choice, randint

_CODE = str

class Generator:

    _LETTERS: list[str] = [chr(position) for position in range(65, 91)]  # - get latin capital letters from ascii chart

    SAMPLE: list[_CODE] = ["WELC-OMET-OTHE", "IEEE-XTRE-ME14", "AAAA-0000-A0A0",
                           "AAAA-0000-A0A1", "AAAA-0000-A0AB", "AAAA-0000-ABAB"]

    @staticmethod
    def load(file_name: str) -> list[_CODE]: return open(file_name, "r").readlines()  # - read pre-generated codes file

    @staticmethod
    def _code() -> list[str, str, str]:  # ------------------ protected method generating a list of three code segments
        out: list = [str().join([choice(Generator._LETTERS) for _ in range(4)]),
                     str().join([str(randint(0, 9)) for _ in range(4)])]
        return out + [str().join([choice(Generator._LETTERS) for _ in range(4)])]

    @staticmethod
    def code() -> _CODE: return str().join(Generator._code())  # ------------------- version without readability dashes

    @staticmethod
    def dash() -> _CODE: return str("-").join(Generator._code())  # ------------------- version with readability dashes

    @staticmethod
    def alter(code: _CODE) -> _CODE:  # --------------------------- remove dashes if they exist, add them if they don't
        assert len(code) in (12, 14)
        if len(code) == 12: code = code[:4] + "-" + code[4:8] + "-" + code[8:]
        elif len(code) == 14: code = code.replace("-", str())
        return code

    def __call__(self, amount: int) -> list[_CODE]: return [self.dash() for _ in range(amount)]  # ----- specify amount


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
                if flag: return False
                else: flag = True
        return True

    def test(self, data: list[_CODE]):
        for left_index, left in enumerate(data):
            for right_index, right in enumerate(data):
                if left_index == right_index: continue
                print(f"DISTANCE OF {left} AND {right}:\t {self.distance(left, right)}")
            print()


if __name__ == "__main__":
    generator = Generator()
    hamming = Hamming()
    data_set: list[_CODE] = generator.SAMPLE
    print(data_set)
    hamming.test(data_set)
