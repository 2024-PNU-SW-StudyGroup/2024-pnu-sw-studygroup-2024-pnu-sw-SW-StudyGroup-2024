N = int(input())
lst=[]

for _ in range(N):
    num = int(input())
    
    if num != 0:
        lst.append(num)
    else:
        lst.pop()
print(sum(lst))