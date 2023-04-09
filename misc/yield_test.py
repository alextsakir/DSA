from functools import wraps
from typing import Callable, Any


# each decorator is a HOF (higher-order function)

def timestamp(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("decorated function: " + func.__name__)
        func(*args, **kwargs)
        return
    return wrapper

def iter_to_loop(func: Callable[[Any], Any]) -> Callable[[Any], Any]:

    def wrap(*args, **kwargs):
        print("decorated function: " + func.__name__)
        return func(*args, **kwargs)
    return wrap

@iter_to_loop
def method(alpha: int) -> int:
    return -alpha


print(method(2))
