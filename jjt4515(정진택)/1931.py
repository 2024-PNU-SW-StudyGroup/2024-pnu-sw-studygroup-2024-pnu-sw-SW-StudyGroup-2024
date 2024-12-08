n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

lst.sort(key = lambda x : (x[1], x[0]))

ans = 0
now = 0 

for s, e in lst:
    if s >= now:
        now = e
        ans += 1
        

print(ans)

