N,M = map(int, input().split())
papers = set(map(int,input().split()))
papersToPrint = [ i for i in list(range(1, N+1)) if i not in papers]
print(papers)
print(papersToPrint)
def cost(k):
    return 5 + 2*k

if len(papersToPrint) == 1:
    print(cost(2))
if len(papersToPrint) == 2 or len(papersToPrint) == 3:
    print(cost(papersToPrint[-1]-papersToPrint[0]+1))
else:
    dp = [0] * len(papersToPrint)
    for i in range(len(papersToPrint)):
        for j in range(len(papersToPrint)-1):
            dp[i] = min(cost(papersToPrint[i:i+j]), dp[i])


