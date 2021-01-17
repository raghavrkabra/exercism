"""Solution to Sieve exercise."""

from math import ceil, sqrt
from typing import List


def primes(limit: int) -> List[int]:
    """Return all the prime numbers smaller then or equal to limit."""
    sieve = [*[False]*2, *[True for _ in range(2, limit+1)]]

    for i in range(ceil(sqrt(len(sieve)))):
        if sieve[i]:
            for j in range(pow(i, 2), limit+1, i):
                sieve[j] = False

    return [i for i in range(len(sieve)) if sieve[i]]
