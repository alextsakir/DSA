class Box:

    def __init__(self):
        self._data: list[int] = [5, 10, 15, 20, 25, 30]
        self._index: int = 0

    def __iter__(self): return self

    def __next__(self):
        if self._index < len(self._data):
            _item = self._data[self._index]
            self._index += 1
            return _item
        else: raise StopIteration


box = Box()

for item in box: print(item)
