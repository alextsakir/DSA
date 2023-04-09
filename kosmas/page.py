from typing import NoReturn, Optional
import string
import random

class Page:
    """
        Class Page is a representation of a page in the disk, each Page is represented as a line in file: 'diskfile.txt'.
        Each Page is 180 bytes and thus, has 3 records(59 bytes each) which contain a key: int(4 bytes) and some data: str(55 bytes).

        In diskfile.txt each line is writen using the binary system.

        You can add records to page using the add_record() method,
        and get record dict using the get_record() method.
    """

    _ID_COUNTER: int = 0

    def __init__(self, records: Optional[dict[int, str]] = {}) -> NoReturn:
        self.__records: Optional[dict[int, str]] = records
        self.page_id: Optional[int] = Page._ID_COUNTER
        Page._ID_COUNTER += 1
        return

    def __str__(self) -> str: return "Page with id=" + str(self.page_id) + " with " + str(
        len(self)) + " records: " + str(self.__records)

    def __len__(self) -> int: return len(self.__records)

    def add_record(self, key: int, value: str) -> NoReturn:
        assert not self.is_full
        self.__records[key] = value

        # print(f"\nPage with id={self.page_id} is full.")
        return

    @property
    def get_records(self) -> dict: return self.__records

    @property
    def is_full(self) -> bool: return len(self) == 3


class Case:

    def __init__(self, name: str, file_path: str, num_of_records: int) -> None:
        self.name: str = name
        self.file_path: str = file_path
        self.num_of_records: int = num_of_records
        self.pages: list[Page] = []

    def make_rand_pages(self) -> NoReturn:
        page: Optional[Page] = None

        for i in range(self.num_of_records):  # TODO ---------------------------------------------------- TO BE CHECKED
            if i % 3 == 0: page = Page()
            if not page.is_full: page.add_record(i, self.rand_str())
            if i % 3 == 2: self.pages.append(page)

        if len(page.get_records) != 3: self.pages.append(page)
        print("LAST PAGE:", self.pages[-1].get_records)
        return  # ----------- wrong --> works only when records/ 3 is whole number (right: 600, wrong: 601, wrong: 602)

    def shuffle_pages(self) -> NoReturn: random.shuffle(self.pages)

    @staticmethod
    def rand_str() -> str: return ''.join(random.choice(string.ascii_letters) for _ in range(55))


if __name__ == "__main__":
    test_case = Case("test", "test.pickle", 12)
    test_case.make_rand_pages()
