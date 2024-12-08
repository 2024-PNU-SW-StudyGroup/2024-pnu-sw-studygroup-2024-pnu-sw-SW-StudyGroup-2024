import heapq
import sys

n=int(input())
max_heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x==0 and len(max_heap) == 0:
        print(0)
    elif x==0:
        result = heapq.heappop(max_heap)[1]
        print(result)
    else:
        heapq.heappush(max_heap, (-x,x))