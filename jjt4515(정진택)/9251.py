line1 = ' ' + input()
line2 = ' ' + input()

dp = [[0] * len(line2) for _ in range(len(line1))]
for i in range(1, len(line1)):
    for j in range(1, len(line2)):
        if line1[i] == line2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])