N = int(input())
num = []
for i in range(N):
    nn = int(input())
    num.append(nn)
    
for k in range(len(num)-1):
    for j in range(len(num)-1):
        if num[j] > num[j+1]:
            tmp = num[j]
            num[j] = num[j+1]
            num[j+1]= tmp
            
for kk in num:
    print(kk)