lis = []
for i in range(9):
    k = int(input())
    lis.append(k)

max_num = max(lis)
ans = lis.index(max_num) + 1
print(max_num)
print(ans)