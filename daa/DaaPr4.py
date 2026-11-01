n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):
    w = int(input("Enter weight: "))
    p = int(input("Enter profit: "))
    weights.append(w)
    profits.append(p)

capacity = int(input("Enter knapsack capacity: "))

# dp = [[0 for j in range(capacity + 1)] for i in range(n + 1)]
dp = []

for i in range(n + 1):
    row = []
    for j in range(capacity + 1):
        row.append(0)
    dp.append(row)

for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(
                profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

print("Maximum Profit =", dp[n][capacity])