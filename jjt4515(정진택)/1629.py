from sys import stdin 
import sys
sys.setrecursionlimit(10**6)

a,b,c = map(int, stdin.readline().split())

def mul(a, n):
    if n == 1:
        return a % c 
    else:
        temp = mul(a, n//2)
        if n % 2 == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * a) % c
        
print(mul(a,b))