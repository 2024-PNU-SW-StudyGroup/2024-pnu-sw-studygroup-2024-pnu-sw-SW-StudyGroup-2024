import sys

loop_num = int(input())
def solve():
    dict_list = []
    n = int(input())
    for i in range(n):
        value, key = sys.stdin.readline().split()
        dict_list.append([key,value])
    count_comb(n, dict_list)
def count_comb(n, dict_list):
    keylist = dict(dict_list).keys()
    d={}
    result = 1
    for i in keylist:
        d[i] = 0
    for i in dict_list:
        key, value = i
        new = d.get(key) + 1
        d[key] = new
    for i in d.values():
        result *= (i+1)
    print(result-1)

for i in range(loop_num):
    solve()
