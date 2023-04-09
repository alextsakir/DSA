from random import seed

from assets import Algorithms, Data

seed(1083879)

if __name__ == "__main__":

    for data in (Data((amount + 1) * 100) for amount in range(5)):
        print(repr(data))
        for algorithm in iter(Algorithms()):
            algorithm(data)
            print(data)
            data.reset()
