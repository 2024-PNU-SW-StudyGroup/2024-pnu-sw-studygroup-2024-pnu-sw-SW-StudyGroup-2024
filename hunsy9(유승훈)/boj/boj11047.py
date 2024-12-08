n,k = map(int,input().split())
coin = [int(input()) for i in range(n)]
avail_coin = [i for i in coin if i <= k]

count = 0

for c in list(reversed(avail_coin)):
    count += (k // c)
    k = k % c
    if k <= 0:
        break
print(count)
