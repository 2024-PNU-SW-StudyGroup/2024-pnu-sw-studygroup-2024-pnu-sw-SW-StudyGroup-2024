n,r,c = map(int, input().split())

num = 2 ** n
end = num * num -1
start = 0

r_start = 0
r_end = num
c_start = 0
c_end = num

while True:
    r_mid = (r_start + r_end) / 2
    c_mid = (c_start + c_end) / 2

    if r < r_mid:
        end = (start + end) // 2
        r_end = r_mid
    elif r >= r_mid:
        start = (start + end) // 2 + 1
        r_start = r_mid
    if c < c_mid:
        end = (start + end) // 2
        c_end = c_mid
    elif c >= c_mid:
        start = (start + end) // 2 + 1
        c_start = c_mid

    if start == end:
        print(start)
        break
    
    
    
        