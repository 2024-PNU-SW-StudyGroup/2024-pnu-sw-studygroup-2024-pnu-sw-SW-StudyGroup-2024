n = int(input())
ans = 0
for num in range(1, n+1):
    if num < 100:
        ans += 1
    else:
        last = num % 10
        mid = (num % 100) // 10
        first = num // 100
        if last - mid == mid - first:
            ans += 1
print(ans)
