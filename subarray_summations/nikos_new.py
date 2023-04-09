from time import time
from random import randint, seed
from typing import Optional


def max_subarray_on3(nums: list[int]):  # ----------------------------------- O(n^3) COMPLEXITY
    summation: int = 0
    left: int = 0
    right: int = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            sum1 = 0
            for k in range(i, j + 1): sum1 += nums[k]
            if sum1 > summation:
                summation = sum1
                left = i
                right = j

    return left, right, summation


def max_subarray_on(nums: list[int]):
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


def max_subarray_on2(nums: list[int]):
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
def max_subarray_nlog_n(nums: list[int]):
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
        right_maximum, total = -1000, 0
        for i in range(middle + 1, right + 1):
            total += numbers[i]
            if total > right_maximum:
                right_maximum = total

        maxLeftRight = max(findMaximumSum(numbers, left, middle), findMaximumSum(numbers, middle + 1, right))

        return max(maxLeftRight, left_maximum + right_maximum)

    return 0, 0, findMaximumSum(nums)
'''

def new_recursive(nums: list[int]):
    left_out, right_out = 0, 0

    def maxCrossingSum(arr, low, m, high, left, right):
        sm = 0
        left_sum = -10000
        for i in range(m, low - 1, -1):
            sm = sm + arr[i]
            if sm > left_sum:
                left_sum = sm

        sm = 0
        right_sum = -1000
        for i in range(m, high + 1):
            sm = sm + arr[i]
            if sm > right_sum:
                right_sum = sm
        return max(left_sum + right_sum - arr[m], left_sum, right_sum)

    def maxSubArraySum(arr, lower, higher):
        # Invalid Range: low is greater than high
        if lower > higher:
            return -10000
        # Base Case: Only one element
        if lower == higher:
            return arr[lower]
        # Find middle point
        m = (lower + higher) // 2
        return max(maxSubArraySum(arr, lower, m - 1), maxSubArraySum(arr, m + 1, higher),
                   maxCrossingSum(arr, lower, m, higher, left_out, right_out))

    summation = maxSubArraySum(nums, 0, len(nums) - 1)

    return left_out, right_out, summation


seed(1083830)

data: list[int] = [randint(-100, 100) for _ in range(200)]  # ------------------------------ list comprehension syntax
answers: list[tuple[int, int, int]] = []  # ------------------------- list of tuples, each consisting of three integers

if __name__ == "__main__":
    print("left\tright\tsum\t\t\ttime")
    for function in [max_subarray_on, max_subarray_on2, max_subarray_on3, max_subarray_nlog_n]:
        start: time = time()
        answers.append(function(data))
        stop: time = time()
        for number in answers[-1]: print(number, end="\t\t")
        print(round(stop - start, 6), "seconds")
