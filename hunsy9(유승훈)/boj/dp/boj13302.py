n, m = map(int,input().split())
dont_visit = list(map(lambda x : int(x) - 1, input().split()))

dp = [[0 for i in range(3)] for i in range(n)]
for i in dont_visit:
    dp[i] = [1,1,1]
print(dp)


