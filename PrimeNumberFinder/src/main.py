# Prime Number Finder.
# It uses the algorithm "Sieve of Eratosthenes" to find all prime numbers
# smaller or equal to a given number n.
# Read more: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

__author__ = 'codinglukas'


def compute_primes(n):
    """
    First we create a boolean array of length n and all entries
    are set to true. In the end the i-th entry will be true
    if and only if i is a prime number.
    :param n:
    :return prime numbers <= n:
    """
    primes = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        # If primes[p] is not changed, then it is a prime
        if primes[p]:
            # Update all multiples of p too
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1
    primes[0] = False
    primes[1] = False

    result = []
    for p in range(n + 1):
        if primes[p]:
            result.append(p)

    return result


if __name__ == '__main__':
    n = 30
    print(compute_primes(n))
