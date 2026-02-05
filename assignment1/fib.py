# fib.py
from functools import lru_cache, wraps
from time import perf_counter
import matplotlib.pyplot as plt
import numpy


x = []
y = []


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"Finished in {end - start:.8f}s: f({args[0]}) -> {result}")
        y.append(end - start)
        return result

    return wrapper


@lru_cache
@timer
def fib(n: int) -> int:
    x.append(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    fib(100)
    x.reverse()
    plt.plot(x, y)
    plt.show()
