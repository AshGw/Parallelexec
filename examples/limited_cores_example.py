import random
import time
from parallelexec import ParallelExec
from typing import Callable, List

_RUNS: int = 10


def one():
    for _ in range(_RUNS):
        print(1 + 2 * random.randint(1, 10))
        time.sleep(0.5)


def two():
    for _ in range(_RUNS):
        print(1 - 2 * random.randint(1, 10))
        time.sleep(0.5)


def three():
    for _ in range(_RUNS):
        print(0)
        time.sleep(0.5)


if __name__ == "__main__":
    callables: List[Callable] = [one, two, three]
    ParallelExec.cores_limited_processor(callables)
