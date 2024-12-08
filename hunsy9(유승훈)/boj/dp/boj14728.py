n, t = map(int, input().split())

ks = [list(map(int, input().split())) for i in range(n)]
dp = [[0 for i in range(t+1)] for i in range(n)]

for danwon in range(0,n):
    for total_time in range(0,t+1):
        # 공부 안할때
        t2 = dp[n-1][total_time]
        t1 = 0
        if ks[danwon][0] <= total_time:
            # n번째 단원을 공부할때 최대 dp[][]
            t1 = dp[n-1][total_time-ks[danwon][0]] + ks[danwon][1]
        dp[danwon][total_time] = max(t1, t2)

print(dp[-1][-1])