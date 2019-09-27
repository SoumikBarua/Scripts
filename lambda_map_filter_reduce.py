# Standard library imports
from functools import reduce

def prime_numbers_under_hundred():
    """Prints a list of all the prime numbers under 100.
    Note: uses a lambda and a filter function to achieve this."""

    # range upto but not including 101
    numbers = range(2, 101)

    # filter the numbers
    # essentially Sieve of Eratosthenes
    for each in range(2, 9):
        numbers = list(filter(lambda x: x==each or x%each, numbers))

    print(numbers)

prime_numbers_under_hundred()
    
def map_and_filter_even_squares(lst):
    """Prints a list with only squares of the even numbers
    in an argument list.
    Note: uses a map and a filter function to achieve this."""
    
    print(list(map(lambda x: x**2, filter(lambda x: x%2==0, lst))))

map_and_filter_even_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def reduce_odd_squares_sum(lst):
    """Prints the sum of squares of only the odd numbers
    in an argument list.
    Note: uses a reduce, a map and a filter function to achieve this."""

    sum_all = reduce(lambda x, y: x + y, map(lambda x: x**2,
                                         filter(lambda x: x%2!=0, lst)))
    print(sum_all)

reduce_odd_squares_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
