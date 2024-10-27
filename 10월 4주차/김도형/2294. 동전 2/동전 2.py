num,total=map(int,input().split())
coin1=set()
for i in range(num):
    a=int(input())
    coin1.add(a)
coin=list(coin1)
dp=[total+1]*(total+1)
dp[0]=0
for i in range(1,total+1):
    for j in coin:
        if i>=j:
            dp[i]=min(dp[i-j]+1,dp[i])
if dp[-1]==total+1:
    print(-1)
else:
    print(dp[-1])

