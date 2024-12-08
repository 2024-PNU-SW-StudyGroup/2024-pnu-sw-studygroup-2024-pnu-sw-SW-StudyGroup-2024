import sys
import heapq
n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline().strip()) for i in range(n)]
hq1, hq2 = [], []
for i in range(n):
    heapq.heappush(hq2, numbers[i])
    if len(hq2) - len(hq1) == 0:
        a = heapq.heappop(hq2)
        heapq.heappush(hq1, -a)
        b = heapq.heappop(hq1)
        heapq.heappush(hq2, -b)
        print(-hq1[0])
    elif len(hq2) - len(hq1) == 1:
        a = heapq.heappop(hq2)
        heapq.heappush(hq1, -a)
        print(-hq1[0])

