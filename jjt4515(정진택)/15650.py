n,m = map(int, input().split())
visited = []

def dfs(s):
    if len(visited) == m:
        print(' '.join(map(str,visited)))
        return 
    
    for i in range(s, n+1):
            visited.append(i)
            dfs(i+1)
            visited.pop()
dfs(1)