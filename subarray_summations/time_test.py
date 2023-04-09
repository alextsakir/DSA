from assets import Algorithms, Data


if __name__ == "__main__":

    for data in (Data(amount * 10 + 5000) for amount in range(51)):
        print(repr(data))
        Algorithms.max_subarray_on2(data)
        print(data)
        if data.duration > 1: break
        data.reset()
