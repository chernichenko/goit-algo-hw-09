import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    coin_count = {}
    
    for coin in coins:
        while amount >= coin:
            amount -= coin
            if coin in coin_count:
                coin_count[coin] += 1
            else:
                coin_count[coin] = 1

    return coin_count

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    coin_count = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in coin_count:
            coin_count[coin] += 1
        else:
            coin_count[coin] = 1
        amount -= coin

    return coin_count

# Тестування і порівняння
amount = 113

# Жадібний алгоритм
start_time = time.time()
greedy_result = find_coins_greedy(amount)
greedy_time = time.time() - start_time

# Алгоритм динамічного програмування
start_time = time.time()
dp_result = find_min_coins(amount)
dp_time = time.time() - start_time

# Виведення результатів
print("Жадібний алгоритм:", greedy_result)
print("Час виконання жадібного алгоритму:", greedy_time)

print("Алгоритм динамічного програмування:", dp_result)
print("Час виконання алгоритму динамічного програмування:", dp_time)