n, m = map(int, input().split())
lst = list(map(int, input().split()))

highest = max(lst)
lowest = 1

while lowest <= highest:
    cut = (highest + lowest) // 2
    ans = 0
    
    for i in range(n):
        if lst[i] > cut:
            ans += lst[i] - cut
    
    if ans >= m:
        lowest = cut + 1
    else:
        highest = cut - 1

print(highest)