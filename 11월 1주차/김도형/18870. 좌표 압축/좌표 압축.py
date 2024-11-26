import sys

n = int(input())
x = list(map(int, sys.stdin.readline().split()))

sorted_x = sorted(set(x))
dic = {sorted_x[i]: i for i in range(len(sorted_x))}

for i in x:
    print(dic[i], end=" ")

