N = int(input()) 
schedule = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)  # dp[i]는 i번째 날부터 N일까지 얻을 수 있는 최대 수익

# DP 계산 (역순으로)
for i in range(N-1, -1, -1):
    time, pay = schedule[i]
    
    # 이번 상담을 끝마칠 수 있는 날이 N일 이내일 경우
    if i + time <= N:
        dp[i] = max(dp[i+1], pay + dp[i + time])
    else:
        dp[i] = dp[i+1]

# 결과 출력
print(dp[0])
