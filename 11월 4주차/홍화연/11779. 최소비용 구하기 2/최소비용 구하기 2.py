import heapq
import sys

input = sys.stdin.read
data = input().splitlines()

# 입력 처리
n = int(data[0])  # 도시의 개수
m = int(data[1])  # 버스의 개수
graph = [[] for _ in range(n + 1)]

# 그래프 구성
for i in range(2, 2 + m):
    u, v, cost = map(int, data[i].split())
    graph[u].append((v, cost))

# 출발점과 도착점
start, end = map(int, data[2 + m].split())

# 다익스트라 알고리즘 구현
def dijkstra(start):
    dist = [float('inf')] * (n + 1)
    prev = [-1] * (n + 1)  # 경로 추적을 위한 배열
    dist[start] = 0
    pq = [(0, start)]  # (비용, 노드)

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        # 이미 처리된 노드라면 무시
        if current_cost > dist[current_node]:
            continue

        # 인접 노드 확인
        for neighbor, weight in graph[current_node]:
            cost = current_cost + weight
            if cost < dist[neighbor]:
                dist[neighbor] = cost
                prev[neighbor] = current_node  # 이전 노드 기록
                heapq.heappush(pq, (cost, neighbor))

    return dist, prev

# 최단 경로 및 경로 추적
dist, prev = dijkstra(start)

# 최소 비용
min_cost = dist[end]

# 경로 추적
path = []
current = end
while current != -1:
    path.append(current)
    current = prev[current]

path.reverse()  # 경로를 역순으로 변환

# 결과 출력
print(min_cost)
print(len(path))
print(" ".join(map(str, path)))
