def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")

    if target == 0:
        return []

    dp = [None] * (target + 1)
    dp[0] = []

    for amount in range(1, target + 1):
        for coin in coins:
            if amount >= coin and dp[amount - coin] is not None:
                result = dp[amount - coin] + [coin]
                if dp[amount] is None or len(result) < len(dp[amount]):
                    dp[amount] = result

    if dp[target] is None:
        raise ValueError("can't make target with given coins")

    return sorted(dp[target])