
n = int(input())
num = 2 ** n - 1
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = []
for i in range(n):
    dp.append([0]*(i+1))

dp[0][0] = graph[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j != 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1])
        if j != i:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
        dp[i][j] += graph[i][j]
print(max(dp[n-1]))
    