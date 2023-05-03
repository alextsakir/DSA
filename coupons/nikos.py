import timeit
import random
from typing import Any, Optional

SIZE = 20
CODE_SIZE: int = 12

print(f"RUNNING WITH SIZE: {SIZE}\n")

def make_codes():
    code_word = ''.join(chr(random.randint(65, 66)) for char in range(4)) + \
                ''.join(str(random.randint(0, 4)) for _ in range(4)) + \
                ''.join(chr(random.randint(65, 66)) for char in range(4))
    return code_word

def insert_func(code_list):
    code_word = make_codes()

    index = sum(ord(char) for char in code_word) % len(code_word)

    code_list[index].insert(0, code_word)

def hamming(string1, string2): return sum([xi != yi for xi, yi in zip(string1, string2)])

def check_codes(code_list) -> list[int]:
    new_code_list = list()
    for element in code_list: new_code_list.append(element)

    distances = [0 for _ in range(SIZE)]
    inner_list_counter: int = 0
    for inner_list_index, inner_list in enumerate(new_code_list):  # for each code list
        if not len(inner_list): continue
        inner_list_counter += 1
        for char_index in range(CODE_SIZE):
            for outer_index in range(len(inner_list)):
                temporary = inner_list[outer_index][:char_index] + "_" + inner_list[outer_index][char_index + 1:]
                for inner_index in range(len(inner_list)):
                    if temporary == inner_list[inner_index] and outer_index != inner_index:
                        print("got here!")
                        distances[inner_list_index] += 1

    print("inner list counter:", inner_list_counter)
    return distances

def analysis(data: list[list]) -> str:
    out: str = "Analysis\n"
    for list_index, c_list in enumerate(data):
        if len(c_list): out += f"List of index {list_index} with {len(c_list)} elements\n"
    count: int = sum(len(c_list) for c_list in data)
    out += f"Total codes in inner lists: {count}\t\t"
    out += "CORRECT" if SIZE == count else "WRONG"
    return out + "\n"


if __name__ == '__main__':
    lista = [[] for _ in range(SIZE)]

    # for i in range(SIZE): insert_func(lista)

    for element in ["WELC-OMET-OTHE", "IEEE-XTRE-ME14", "AAAA-0000-A0A0", "AAAA-0000-A0A1",
                    "AAAA-0000-A0AB", "AAAA-0000-ABAB"]:
        index = sum(ord(char) for char in element) % len(lista)
        lista[index].insert(0, element)

    dist = check_codes(lista)
    print(lista)
    print(analysis(lista))
    print(dist)
