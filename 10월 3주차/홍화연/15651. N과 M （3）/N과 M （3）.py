def dfs(N, M, sequence):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, N + 1):
        dfs(N, M, sequence + [i])

# 입력
N, M = map(int, input().split())

# 수열을 출력하기 위해 DFS 실행
dfs(N, M, [])
