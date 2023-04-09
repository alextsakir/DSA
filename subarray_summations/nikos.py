"""                                           Saturday 18 Mar 2023

Here comes another approach of the problem, in terms of storing and displaying the results in an easier way. Instead
of having to create a new class from scratch, the results can be stored as tuples of three integers.
Each one stores the answer that an algorithm gave, having left, right and sum.
"""

from time import time
from random import randint, seed
from typing import Optional


def max_subarray(nums: list[int]) -> tuple[int, int, int]:  # --------------------------- O(n) COMPLEXITY - NOT WORKING
    summation: int = nums[0]
    left: int = 0
    right: int = 0
    max_ending_here: int = nums[0]
    for index in range(len(nums)):
        # max_ending_here = nums[index] + max_ending_here if nums[index] + max_ending_here > nums[index] else nums[index]
        # summation = max_ending_here if summation < max_ending_here else summation

        if max_ending_here > 0:
            max_ending_here += nums[index]
            right = index
        else:
            max_ending_here = nums[index]
            left = index

        if summation < max_ending_here: summation = max_ending_here

    return left, right, summation


def max_subarray_on3(nums: list[int]) -> tuple[int, int, int]:  # ----------------------------------- O(n^3) COMPLEXITY
    summation: int = 0
    left: int = 0
    right: int = 0
    sum1: int = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            sum1 = 0
            for k in range(i, j + 1): sum1 += nums[k]
            if sum1 > summation:
                summation = sum1
                left = i
                right = j

    return left, right, summation


def kadane(nums: list[int]) -> tuple[int, int, int]:
    summation = 0
    left: int = 0
    right: int = 0
    temporary_sum: int = 0
    temporary_left: int = 0

    for i in range(len(nums)):
        if not temporary_sum: temporary_left = i
        temporary_sum += nums[i]
        if temporary_sum > summation:
            summation = temporary_sum
            right = i
            left = temporary_left

        if temporary_sum < 0:
            temporary_sum = 0

    return left, right, summation


def kadane_indices(nums: list[int]) -> tuple[int, int, int]:
    summation, temporary_left, left, right, current_max = nums[0], 0, 0, 0, nums[0]
    for index in range(1, len(nums)):
        if current_max < 0:
            current_max = nums[index]
            temporary_left = index
        else:
            current_max += nums[index]
        temporary_right = index
        if current_max > summation:
            summation = current_max
            left = temporary_left
            right = temporary_right

    return left, right, summation


def our_method(nums: list[int]) -> tuple[int, int, int]:
    left, right, temporary_left, temporary_right, summation, only_negatives = 0, 0, 0, 0, 0, True
    for element in nums:
        if number > 0: only_negatives = False

    for temporary_left in range(len(nums)):  # ------------------------------------------------------------- outer loop
        if not only_negatives and nums[temporary_left] < 0: continue
        subarray: list[int] = list()
        subarray.append(nums[temporary_left])
        for temporary_right in range(temporary_left, len(nums)):  # ---------------------------------------- inner loop
            if temporary_left != temporary_right: subarray.append(nums[temporary_right])
            temp = sum(subarray)
            if temp > summation: left, right, summation = temporary_left, temporary_right, temp

    return left, right, summation


def max_subarray_on2(nums: list[int]) -> tuple[int, int, int]:
    left, right, summation, temporary_left, temporary_right, temporary_sum = 0, 0, 0, 0, 0, 0
    for i in range(len(nums)):
        if not temporary_sum and nums[i] < 0: continue  # -- without this, we would have (1+2+3+...+n) total iterations
        temporary_left = i
        for j in range(i, len(nums)):
            temporary_sum += nums[j]
            temporary_right = j
            if temporary_sum > summation:
                summation, left, right = temporary_sum, temporary_left, temporary_right
        temporary_sum = 0
    return left, right, summation

'''
def max_subarray_recursive(nums: list[int]) -> tuple[int, int, int]:
    left_index, right_index = 0, 0

    def findMaximumSum(numbers: list[int], left: Optional[int] = None, right: Optional[int] = None) -> int:
        if not numbers: return 0
        if left is None and right is None: left, right = 0, len(numbers) - 1
        if right == left: return numbers[left]
        middle = (left + right) // 2

        left_maximum, total = -1000, 0
        for i in range(middle, left - 1, -1):
            total += numbers[i]
            if total > left_maximum:
                left_maximum = total
                left_index = i

        right_maximum, total = -1000, 0

        for i in range(middle + 1, right + 1):
            total += numbers[i]
            if total > right_maximum:
                right_maximum = total
                right_index = i

        maxLeftRight = max(findMaximumSum(numbers, left, middle), findMaximumSum(numbers, middle + 1, right))

        if findMaximumSum(numbers, left, middle) > findMaximumSum(numbers, middle + 1, right):
            left_index = left
            right_index = middle
        else:
            left_index = middle + 1
            right_index = right

        return max(maxLeftRight, left_maximum + right_maximum)

    return 0, 0, findMaximumSum(nums)
'''

def new_recursive(nums: list[int]) -> tuple[int, int, int]:
    left_out, right_out = 0, 0

    def maxCrossingSum(arr, l, m, h, left, right):

        sm = 0
        left_sum = -10000
        for i in range(m, l - 1, -1):
            sm = sm + arr[i]
            if sm > left_sum:
                left_sum = sm

        sm = 0
        right_sum = -1000
        for i in range(m, h + 1):
            sm = sm + arr[i]
            if sm > right_sum:
                right_sum = sm

        return max(left_sum + right_sum - arr[m], left_sum, right_sum)

    def maxSubArraySum(arr, l, h):
        # Invalid Range: low is greater than high
        if l > h:
            return -10000
        # Base Case: Only one element
        if l == h:
            return arr[l]

        # Find middle point
        m = (l + h) // 2

        return max(maxSubArraySum(arr, l, m - 1), maxSubArraySum(arr, m + 1, h),
                   maxCrossingSum(arr, l, m, h, left_out, right_out))

    summation = maxSubArraySum(nums, 0, len(nums) - 1)

    return left_out, right_out, summation

# seed(1083830)


data: list[int] = [randint(-100, 100) for _ in range(500)]  # ------------------------------ list comprehension syntax
answers: list[tuple[int, int, int]] = []  # ------------------------- list of tuples, each consisting of three integers

if __name__ == "__main__":
    print("LEFT\tRIGHT\tSUM\t\t\tTIME")
    for function in [kadane_indices, max_subarray_on2, max_subarray_on3, max_subarray_recursive]:
        start: time = time()
        answers.append(function(data))
        stop: time = time()
        for number in answers[-1]: print(number, end="\t\t")
        print(round(stop - start, 6), "seconds")

    print("\n\n", data[answers[2][0]: answers[2][1] + 1])
