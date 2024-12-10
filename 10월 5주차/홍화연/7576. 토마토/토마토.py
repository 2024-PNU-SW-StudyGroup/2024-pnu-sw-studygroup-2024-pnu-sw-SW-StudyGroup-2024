from collections import deque

def tomato_ripening_days(M, N, box):
    # 방향 벡터: 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 익은 토마토 위치를 저장할 큐 및 초기 상태 설정
    queue = deque()
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                queue.append((i, j))
    
    # BFS 시작
    days = -1  # 첫날은 0일로 시작, 마지막 레벨을 일수로 계산
    while queue:
        days += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                    box[nx][ny] = 1  # 익음 처리
                    queue.append((nx, ny))
    
    # 익지 않은 토마토가 있는지 확인
    for row in box:
        if 0 in row:
            return -1
    
    return days if days != -1 else 0

# 입력 처리
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(tomato_ripening_days(M, N, box))

