"""
A number’s factors are any two other numbers
that, when multiplied with each other,
produce the number. For example, 2 × 13 =
26, so 2 and 13 are factors of 26. Also, 1 × 26 =
26, so 1 and 26 are also factors of 26. Therefore, we
say that 26 has four factors: 1, 2, 13, and 26.

"""

from math import sqrt
from collections import OrderedDict
from timeit import default_timer as timer


def divisible(number, factor):
    return number % factor == 0


def factors_for_odd_number(number):
    factors = [1, number]
    for i in range(3, sqrt(number) + 1, 2):
        if divisible(number, i):
            factors.append(i)
            factors.append(number // i)
    return factors


def factors_for_even_number(number):
    factors = [1, number]
    for i in range(2, int(sqrt(number) + 1)):
        if divisible(number, i):
            factors.append(i)
            factors.append(number // i)
    return factors


def remove_duplicates(factors):
    return list(OrderedDict.fromkeys(factors))


def main():
    print("Enter a number to find its factors: ")
    number = int(input())

    timer_start = timer()

    if number % 2 == 0:
        factors = factors_for_even_number(number)
    else:
        factors = factors_for_odd_number(number)
    factors.sort()
    print("time taken: ", timer() - timer_start)
    print(remove_duplicates(factors))


if __name__ == "__main__":
    main()
