#!/usr/bin/python3
"""Module defining isWinner function."""


def isWinner(x, nums):
    """
    Determines the winner of the prime game played between Maria and Ben.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the maximum number in each round.

    Returns:
        str: Name of the player that won the most rounds, or None if it's a tie.
    """
    if not nums or x < 1:
        return None

    # Helper function to generate a list of primes up to the maximum number in nums
    def sieve_of_eratosthenes(max_num):
        primes = [True] * (max_num + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(max_num ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, max_num + 1, i):
                    primes[j] = False
        return primes

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
