from itertools import combinations
from collections import deque
import copy

# 입력 받기
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

# 방향 벡터 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 빈 칸과 바이러스 위치 저장
empty_spaces = []
virus_positions = []

for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty_spaces.append((i, j))
        elif lab[i][j] == 2:
            virus_positions.append((i, j))

# 바이러스 확산 함수
def spread_virus(temp_lab):
    queue = deque(virus_positions)
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and temp_lab[nx][ny] == 0:
                temp_lab[nx][ny] = 2
                queue.append((nx, ny))

# 안전 영역 계산 함수
def get_safe_area(temp_lab):
    return sum(row.count(0) for row in temp_lab)

# 최대 안전 영역 계산
max_safe_area = 0

# 빈 칸에 3개의 벽을 세우는 모든 조합을 시도
for walls in combinations(empty_spaces, 3):
    # 연구소 복사
    temp_lab = copy.deepcopy(lab)
    
    # 벽 세우기
    for x, y in walls:
        temp_lab[x][y] = 1
    
    # 바이러스 확산
    spread_virus(temp_lab)
    
    # 안전 영역 크기 계산
    max_safe_area = max(max_safe_area, get_safe_area(temp_lab))

# 결과 출력
print(max_safe_area)

