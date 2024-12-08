n = int(input())
cnt = 0
lst = [float('inf')] * (n+1)

lst[0] = 0
lst[1] = 1



for i in range(2, n+1):
    j = 2
    min_value = lst[i-1]
    while i - j**2 >= 0:
        if lst[i-j**2] < min_value:
            min_value = lst[i-j**2]
        j += 1

    lst[i] = min_value + 1

print(lst[n])
