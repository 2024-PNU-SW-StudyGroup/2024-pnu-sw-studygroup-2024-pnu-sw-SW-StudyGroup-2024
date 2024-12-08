n= int(input())
grape_whisky = [ int(input()) for i in range(n) ]

dp = [[0 for i in range(3)] for i in range(n)]

dp[0][0] = 0
dp[0][1] = grape_whisky[0]
dp[0][2] = 0

maxNum = 0
for i in range(1, n):
    dp[i][0] = max(dp[i - 1])
    dp[i][1] = dp[i - 1][0] + grape_whisky[i]
    dp[i][2] = dp[i - 1][1] + grape_whisky[i]
    # print("dpTable: ",dp)
print(max(dp[n-1]))
