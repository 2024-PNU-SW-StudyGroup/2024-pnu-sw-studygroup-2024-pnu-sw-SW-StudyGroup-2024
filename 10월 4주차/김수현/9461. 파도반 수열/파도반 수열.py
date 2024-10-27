num = int(input())

def padoban(n):
    if memo[n] != -1:
        return memo[n]
    if n <= 3:
        memo[n] = 1
    elif 3 < n <= 5:
        memo[n] = 2
    else:
        memo[n] = padoban(n-5) + padoban(n-1)
        
    return memo[n]

for i in range(num):
    N = int(input())
    memo = [-1 for j in range(N+1)]
    
    print(padoban(N))
    
    
    
    