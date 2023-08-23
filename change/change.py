def find_fewest_coins(coins, target):
    if target == 0:
        return []

    if target < 0:
        raise ValueError("target can't be negative")

    if min(coins) > target:
        raise ValueError("can't make target with given coins")

    dp = [float("inf")] * (target + 1)
    dp[0] = 0
    coin_used = [
        [] for _ in range(target + 1)
    ]  # List to store used coins for each amount

    for i in range(1, target + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin_used[i - coin] + [coin]

    if dp[target] == float("inf"):
        raise ValueError("can't make target with given coins")

    return list(reversed(coin_used[target]))
