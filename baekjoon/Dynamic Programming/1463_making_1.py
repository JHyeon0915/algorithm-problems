import math

target = int(input())

dp = [0] * (target + 1)
for i in range(2, target + 1):
    one, two, three = math.inf, math.inf, dp[i-1]
    if i % 3 == 0:
        one = min(dp[i-1], dp[i//3])
    if i % 2 == 0:
        two = min(dp[i-1], dp[i//2])

    dp[i] = 1 + min(one, two, three)

print(dp[target])