"""Solution to Sieve exercise."""

from typing import List


def primes(limit: int) -> List[int]:
    """Return all the prime numbers smaller then or equal to limit."""
    sieve = dict.fromkeys(range(2, limit+1), True)

    for key in iter(sieve):
        if sieve[key] is True:
            for i in range(pow(key, 2), limit+1, key):
                sieve[i] = False

    return [key for key in sieve if sieve[key] is True]
