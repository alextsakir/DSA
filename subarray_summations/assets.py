"""                                           Thursday 16 Mar 2023

Για ένα πίνακα τυχαίων ακεραίων αριθμών (θετικών και αρνητικών) ζητείται η υλοποίηση αλγορίθμων εύρεσης του υπο-πίνακα
(συνεχόμενες τιμές) που το άθροισμα των στοιχείων του είναι μέγιστο.
Απαιτείται να προσδιορισθεί η τιμή του αθροίσματος καθώς και οι θέσεις στον αρχικό πίνακα που ξεκινά και σταματά ο
υποπίνακας.
"""

from random import randint
from time import time, gmtime
from typing import NoReturn, Optional, List, Tuple, Iterable


class Data:

    MAX_ABS_VALUE: int = 100
    INVALID_INDEX: int = -1

    __slots__: Tuple[str] = ("amount", "numbers", "left", "right", "summation", "iterations",
                             "description", "start_time", "end_time")

    def __init__(self, amount: int = 1000) -> NoReturn:
        self.amount: int = amount
        self.numbers: List[int] = []
        self.left: int = 0
        self.right: int = 0
        self.summation: int = 0
        self.iterations: int = 0
        self.description: str = str()
        self.start_time: Optional[time] = None
        self.end_time: Optional[time] = None
        for element in range(amount): self.numbers.append(randint(-Data.MAX_ABS_VALUE, Data.MAX_ABS_VALUE))
        return

    @property
    def duration(self) -> int:
        try: assert self.end_time is not None and self.start_time is not None
        except AssertionError: print("start_time and end_time are not set!")
        return round(self.end_time - self.start_time, 4)

    def __repr__(self) -> str: return f"DATA SET: {self.amount} numbers"

    def __str__(self) -> str:
        out: str = f"FINAL ANSWER:\t Subarray of {self.right - self.left + 1} numbers from position "
        out += f"{self.left} until position {self.right} with sum: {self.summation}"
        out += " " * (100 - len(out)) + f"Duration: {self.duration} seconds"
        out += " " * (130 - len(out)) + f"Total iterations: {self.iterations}"
        return out + " " * (165 - len(out)) + "Description: " + self.description

    def __eq__(self, other) -> bool: return self.numbers == other.numbers

    @property
    def subarray(self) -> str:
        return "\nSUBARRAY: " + str().join([str(self.numbers[i]) + "   " for i in range(self.left, self.right + 1)])

    def reset(self) -> NoReturn:
        self.summation, self.left, self.right = 0, 0, 0
        self.start_time, self.end_time, self.description = None, None, str()
        return


class Algorithms:

    def __iter__(self) -> Iterable: return iter([Algorithms.my_method, Algorithms.max_subarray_on,
                                                 Algorithms.max_subarray_on2, Algorithms.max_subarray_on3,
                                                 Algorithms.max_subarray_recursive])

    @staticmethod
    def my_method(data: Data) -> NoReturn:
        data.description = "Another method with O(n^2)"
        data.start_time = time()  # ------------------------------------------------------------------------ START TIME
        only_negatives: bool = True
        for number in data.numbers:
            if number > 0: only_negatives = False

        for left in range(len(data.numbers)):  # ----------------------------------------------------------- OUTER LOOP
            if not only_negatives and data.numbers[left] < 0: continue
            subarray: list[int] = [data.numbers[left]]
            for right in range(left, len(data.numbers)):  # ------------------------------------------------ INNER LOOP
                data.iterations += 1
                if left != right: subarray.append(data.numbers[right])
                if sum(subarray) > data.summation: data.left, data.right, data.summation = left, right, sum(subarray)
        data.end_time = time()  # ---------------------------------------------------------------------------- END TIME
        return

    @staticmethod
    def max_subarray_on(data: Data) -> NoReturn:  # --------------------------------------------------- O(n) COMPLEXITY
        data.description = "Method with O(n) [Kadane]"
        current_max: int = data.numbers[0]
        temporary_left: int = 0
        data.start_time = time()  # ------------------------------------------------------------------------ START TIME

        for index in range(1, len(data.numbers)):
            if current_max < 0:
                current_max = data.numbers[index]
                temporary_left = index
            else:
                current_max += data.numbers[index]
            temporary_right = index
            if current_max > data.summation:
                data.summation = current_max
                data.left = temporary_left
                data.right = temporary_right

        data.end_time = time()  # ---------------------------------------------------------------------------- END TIME
        return

    @staticmethod
    def max_subarray_on2(data: Data) -> NoReturn:
        data.description = "Method with O(n^2)"
        temporary_left, temporary_right, temporary_sum = 0, 0, 0
        data.start_time = time()  # ------------------------------------------------------------------------ START TIME
        for i in range(len(data.numbers)):
            if not temporary_sum and data.numbers[i] < 0:
                continue  # -------------------------------- WITHOUT THIS, WE WOULD HAVE (1+2+3+...+n) TOTAL ITERATIONS
            temporary_left = i
            for j in range(i, len(data.numbers)):
                data.iterations += 1
                temporary_sum += data.numbers[j]
                temporary_right = j
                if temporary_sum > data.summation:
                    data.summation, data.left, data.right = temporary_sum, temporary_left, temporary_right
            temporary_sum = 0
        data.end_time = time()  # ---------------------------------------------------------------------------- END TIME
        return

    @staticmethod
    def max_subarray_on3(data: Data) -> NoReturn:  # ------------------------------------------------ O(n^3) COMPLEXITY
        data.description = "Method with O(n^3)"
        data.start_time = time()  # ------------------------------------------------------------------------ START TIME
        for i in range(len(data.numbers)):
            for j in range(i, len(data.numbers)):
                temporary = 0
                for k in range(i, j + 1):
                    data.iterations += 1
                    temporary += data.numbers[k]
                if temporary > data.summation:
                    data.summation = temporary
                    data.left = i
                    data.right = j
        data.end_time = time()  # ---------------------------------------------------------------------------- END TIME
        return

    @staticmethod
    def max_subarray_recursive(data: Data) -> NoReturn:
        data.description = "Recursive method with O(n * log(n))"
        data.start_time = time()  # ------------------------------------------------------------------------ START TIME

        def findMaximumSum(numbers: list[int], left: Optional[int] = None, right: Optional[int] = None) -> int:
            if not numbers: return 0
            if left is None and right is None: left, right = 0, len(numbers) - 1
            if right == left: return numbers[left]
            middle = (left + right) // 2

            left_maximum, total = -Data.MAX_ABS_VALUE, 0
            for index in range(middle, left - 1, -1):
                total += numbers[index]
                if total > left_maximum: left_maximum = total

            right_maximum, total = -Data.MAX_ABS_VALUE, 0
            for index in range(middle + 1, right + 1):
                total += numbers[index]
                if total > right_maximum: right_maximum = total

            maxLeftRight = max(findMaximumSum(numbers, left, middle), findMaximumSum(numbers, middle + 1, right))
            return max(maxLeftRight, left_maximum + right_maximum)
        data.summation = findMaximumSum(data.numbers)
        data.left, data.right, data.iterations = Data.INVALID_INDEX, Data.INVALID_INDEX, Data.INVALID_INDEX
        data.end_time = time()  # ---------------------------------------------------------------------------- END TIME
        return


if __name__ == "__main__":
    print(gmtime(0))

    print("\nAssets classes methods and properties:\n")
    for cls in Data, Algorithms:
        print(cls.__name__, [method for method in dir(cls) if not method.startswith("_")])
