import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

r_start = 0
r_end = n-1
c_start = 0
c_end = n-1

white = 0
blue = 0

def fun(r_start, r_end, c_start, c_end):
    global white, blue
    state = graph[r_start][c_start] 
    for r in range(r_start, r_end + 1):
        for c in range(c_start, c_end + 1):
            if state != graph[r][c]:
                r_mid = (r_start + r_end) // 2
                c_mid = (c_start + c_end) // 2
                fun(r_start, r_mid, c_start, c_mid)
                fun(r_start, r_mid, c_mid+1, c_end)
                fun(r_mid+1, r_end, c_start, c_mid)
                fun(r_mid+1, r_end, c_mid+1, c_end)
                return 
    if state == 0:
        white += 1
    elif state == 1:
        blue += 1
            
fun(r_start, r_end, c_start, c_end)
print(white)
print(blue)