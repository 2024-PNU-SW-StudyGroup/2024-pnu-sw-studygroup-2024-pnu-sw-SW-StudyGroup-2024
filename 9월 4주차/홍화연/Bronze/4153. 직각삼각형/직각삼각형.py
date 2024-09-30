while True:
    A,B,C = map(int, input().split())
    
    if A == B == C == 0:
        break
    
    lst = [A,B,C]
    tri = sorted(lst)
    
    if (tri[2])**2 == (tri[0])**2 + (tri[1])**2:
        print('right')
    else:
        print('wrong')