#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    :param coins: List of the values of the coins in your possession.
    :param total: Total amount to achieve using the fewest coins.
    :return: Fewest number of coins needed, or -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)
    num_coins = 0
    remaining = total

    for coin in coins:
        if remaining <= 0:
            break
        count = remaining // coin
        num_coins += count
        remaining -= count * coin

    # If we still have a remaining amount, we can't make the exact total
    if remaining > 0:
        return -1

    return num_coins
