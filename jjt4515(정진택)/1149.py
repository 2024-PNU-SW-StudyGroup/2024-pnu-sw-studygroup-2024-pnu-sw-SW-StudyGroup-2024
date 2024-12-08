n = int(input())
graph = [[0, 0, 0]]
for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

dp = [[0] * (n+1) for _ in range(3)]
for i in range(1, n+1):
    dp[0][i] = min(dp[1][i-1], dp[2][i-1]) + graph[i][0]
    dp[1][i] = min(dp[0][i-1], dp[2][i-1]) + graph[i][1]
    dp[2][i] = min(dp[0][i-1], dp[1][i-1]) + graph[i][2]

print(min(dp[0][-1], dp[1][-1], dp[2][-1]))