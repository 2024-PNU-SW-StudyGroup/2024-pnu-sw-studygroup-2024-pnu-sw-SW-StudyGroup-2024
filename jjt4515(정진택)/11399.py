n = int(input())
lst = list(map(int, input().split()))
ans = [0] * n

lst.sort()

ans[0] = lst[0]
for i in range(1, n):
    ans[i] = lst[i] + ans[i-1]
print(sum(ans))