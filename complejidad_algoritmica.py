import time
import sys


def factorial(n: int) -> int:
    """Generates the factorial of an integer iteratively.

    Args:
        n (int): The integer for which the factorial will be calculated.

    Returns:
        int: The factorial of the given number.
    """
    result = 1
    # Loop to calculate the factorial iteratively
    while n > 1:
        result *= n
        n -= 1
    return result


def factorial_r(n: int) -> int:
    """Generates the factorial of an integer recursively.

    Args:
        n (int): The integer for which the factorial will be calculated.

    Returns:
        int: The factorial of the given number.
    """
    # Base case: the factorial of 0 and 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive call to calculate the factorial
    return n * factorial_r(n - 1)


if __name__ == '__main__':
    n = 200000

    # Measure the time taken to calculate the factorial iteratively
    start = time.time()
    factorial(n)
    end = time.time()
    print(f"Iterative factorial took {end - start:.6f} seconds")

    # Increase the recursion limit (caution: can be risky)
    sys.setrecursionlimit(n + 10)

    # Measure the time taken to calculate the factorial recursively
    start = time.time()
    try:
        factorial_r(n)
    except RecursionError:
        print("RecursionError: maximum recursion depth exceeded")
    end = time.time()
    print(f"Recursive factorial took {end - start:.6f} seconds")
