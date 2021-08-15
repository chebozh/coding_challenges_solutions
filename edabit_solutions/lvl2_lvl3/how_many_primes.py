"""How Many "Prime Numbers" Are There?

Create a function that finds how many prime numbers there are, up to the given integer.
Examples

prime_numbers(10) ➞ 4
# 2, 3, 5 and 7

prime_numbers(20) ➞ 8
# 2, 3, 5, 7, 11, 13, 17 and 19

prime_numbers(30) ➞ 10
# 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29
"""


def prime_numbers(num):
    primes = 0
    for n in range(2, num + 1):
        if is_prime(n):
            primes += 1
    return primes


def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return False


if __name__ == '__main__':
    assert prime_numbers(10) == 4
    # 2, 3, 5 and 7

    assert prime_numbers(20) == 8
    # 2, 3, 5, 7, 11, 13, 17 and 19

    assert prime_numbers(30) == 10
    # 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29
