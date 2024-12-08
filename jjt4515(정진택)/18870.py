from sys import stdin 
n = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
s = set(lst)
s = sorted(s)

dic = {}
for i in range(len(s)):
    dic[s[i]] = i

for i in lst:
    print(dic[i], end=" ")