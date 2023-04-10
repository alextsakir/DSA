import timeit
import random


def hamming_distance(string1, string2): ...


# dist_counter = 0
# for n in range(len(string1)):
# if string1[n] != string2[n]:
# dist_counter += 1
# return dist_counter

# or return sum([xi != yi for xi, yi in zip(string1, string2)])

# test Coupon Codes

def test_codes():
    return ["WELC-OMET-OTHE", "IEEE-XTRE-ME14", "AAAA-0000-A0A0", "AAAA-0000-A0A1", "AAAA-0000-A0AB", "AAAA-0000-ABAB"]


# ---
# make a list with num random different Coupon Codes
# --------------------------------------------------
def make_codes(num):
    letters = 'ABCDE'  # FGHIJK' # smaller set for testing
    digits = '012345'
    scode, lcode = set(), []
    while True:
        code = ''.join(random.sample(letters, 4)) + '-' + \
               ''.join(random.sample(digits, 4)) + '-' + \
               ''.join(random.sample(letters, 4))
        if code not in scode:  # check for code in set, not in list
            lcode.append(code)
        scode.add(code)
        if len(lcode) == num:
            return lcode


# ---
# solve using 2 loops
# ---------------------------
def solve_2_loops(code_list):
    t0 = timeit.default_timer()

    n = len(code_list)
    c = 0
    for i1 in range(n - 1):
        for i2 in range(i1 + 1, n):
            if hamming_distance(code_list[i1], code_list[i2]) == 1:
                c += 1
                print(f'({i1 + 1:4d},{i2 + 1:4d}) {code_list[i1]} {code_list[i2]}')

    print(f'πλήθος κωδικών: {n}, ζεύγη παραπλήσιων κωδικών: {c}')
    print(f'time={timeit.default_timer() - t0:.2f}')


if __name__ == "__main__":
    # code_list = test_codes()

    random.seed(123)
    code_list = make_codes(1_000)

    solve_2_loops(code_list)
