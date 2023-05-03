from datetime import datetime, time, date, timedelta
from typing import NoReturn, Optional

class Timer:

    class _Element:
        def __init__(self, label: Optional[str] = None) -> NoReturn:
            self.time: time = datetime.now().time()
            self.label: str = label if label else str()
            return

        def __str__(self) -> str: return str(self.time) + "\t\t" + self.label

        def __sub__(self, other) -> timedelta:
            return datetime.combine(date.min, self.time) - datetime.combine(date.min, other.time)

    def __init__(self, name: Optional[str] = None) -> NoReturn:
        self.name: str = name if name else "New Timer"
        self._store: list[Timer._Element] = list()
        return

    def __len__(self) -> int: return len(self._store)

    def __str__(self) -> str:
        out: str = self.name + ":\n"
        if not len(self): return out
        elif len(self) == 1: return out + str(self._store[0])
        for index in range(len(self) - 1):
            print("index -> ", index)
            out += str(self._store[index]) + "\n\t" + str(self._store[index + 1] - self._store[index]) + "\n"
        return out + str(self._store[-1])

    def note(self, label: Optional[str] = None) -> "Timer._Element":
        element: Timer._Element = Timer._Element(label)
        self._store.append(element)
        return element


if __name__ == "__main__":
    timer = Timer("MyTimer")
    timer.note("start")
    a = -10
    for _ in range(9000000): a += 2
    timer.note("medium")
    a = -10
    for _ in range(90000000): a += 2
    timer.note("stop")

    print(timer)
