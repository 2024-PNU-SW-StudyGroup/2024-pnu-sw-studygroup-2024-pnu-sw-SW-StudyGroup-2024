from collections import deque

N = int(input())
grid = [list(input().strip()) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y, color, is_colorblind):
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                
                if is_colorblind:
                    if color in "RG" and grid[nx][ny] in "RG":
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                    elif color == "B" and grid[nx][ny] == "B":
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                
                else:
                    if grid[nx][ny] == color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

def count_regions(is_colorblind):
    global visited
    visited = [[False] * N for _ in range(N)]
    region_count = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j, grid[i][j], is_colorblind)
                region_count += 1

    return region_count


normal_count = count_regions(is_colorblind=False) 
colorblind_count = count_regions(is_colorblind=True) 
print(normal_count, colorblind_count)
