import random
import time
from parallelexec import ParallelExec

_RUNS: int = 4


@ParallelExec.thread(join=True)
def one():
    for _ in range(_RUNS):
        print(54 + 64 * random.randint(1, 10))
        time.sleep(0.5)


@ParallelExec.thread(join=True)
def two():
    for _ in range(_RUNS):
        print(54 - 64 * random.randint(1, 10))
        time.sleep(0.5)


@ParallelExec.thread(join=True)
def three():
    for _ in range(_RUNS):
        print(0)
        time.sleep(0.5)


if __name__ == "__main__":
    print("before it runs all these functions")
    one()
    two()
    print(
        "if join is set to true this should only show up if:"
        " one() & two() have finished executing"
    )
    three()
    print("If join then this is last thing that shows up")
