"""Sum of Prime Numbers

Create a function that takes a list of numbers and returns the sum of all prime numbers in the list.
Examples

sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17

sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87

sum_primes([]) ➞ None

Notes

    Given numbers won't exceed 101.
    A prime number is a number which has exactly two divisors."""


def sum_primes(lst):
    if not lst:
        return None
    primes = [num for num in lst if is_prime(num)]
    return sum(primes)


def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return False


if __name__ == '__main__':
    assert sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 17

    assert sum_primes([2, 3, 4, 11, 20, 50, 71]) == 87

    assert sum_primes([]) is None
