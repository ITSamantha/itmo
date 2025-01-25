"""
This module contains functions to calculate the length of recurring cycles
in decimal fractions and find the number with the longest recurring cycle
for numbers less than a given limit.
"""

def count_recurring_cycle_length(n: int, d: int) -> int:
    """
    Counts the length of the recurring cycle in the decimal fraction
    representation of n/d.

    Args:
        n (int): The numerator.
        d (int): The denominator.

    Returns:
        int: The length of the recurring cycle in the decimal fraction.
    """
    for i in range(1, d):
        if n == 10 ** i % d:
            return i
    return 0


def count_longest_recurring_cycle(n: int) -> int:
    """
    Finds the number less than n with the longest recurring cycle
    in its decimal fraction representation.

    Args:
        n (int): The upper limit for the search.

    Returns:
        int: The number with the longest recurring cycle length.
    """
    start_number = 2
    max_length = 0
    d = start_number

    for i in range(start_number, n):
        if i % 5 == 0:
            continue

        length: int = count_recurring_cycle_length(1, i)

        if length > max_length:
            max_length = length
            d = i

    return d


def main() -> None:
    """
    The main function to find and print the number with the longest
    recurring cycle for denominators less than 1000.
    """
    number: int = 1000
    result: int = count_longest_recurring_cycle(number)
    print(f"Result value d={result} for d<{number}.")


if __name__ == "__main__":
    main()
    