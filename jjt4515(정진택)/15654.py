n, m = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()

def backtracking(depth):
    if depth == m:
        print(' '.join(map(str,visited)))
        return
    for i in range(n):
        if lst[i] in visited:
            continue
        visited.append(lst[i])
        backtracking(depth + 1)
        visited.pop()
    

visited = []
backtracking(0)


