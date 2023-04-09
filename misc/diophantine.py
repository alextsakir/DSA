"""                                           Sunday 19 Mar 2023

Code that finds solutions for Diophantine equation:
1² + 2² + 3² + ... + x² = y²

"""

def is_square(integer: int) -> bool: return True if integer ** (1 / 2) == int(integer ** (1 / 2)) else False


if __name__ == "__main__":

    LIMIT: int = 100_000

    for number in range(LIMIT + 1):
        summation: int = 0
        for term in range(number + 1): summation += number ** 2
        if is_square(summation): print(number, summation)
