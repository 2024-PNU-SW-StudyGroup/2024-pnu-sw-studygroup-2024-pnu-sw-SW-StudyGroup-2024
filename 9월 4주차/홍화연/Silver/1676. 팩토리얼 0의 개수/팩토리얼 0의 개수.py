N = int(input())
num = 1

for i in range(2,N+1):
    num *= i
    
num_lst = [int(digit) for digit in str(num)][::-1]

answer = 0
for i in range(len(num_lst)):
    if num_lst[i] == 0:
        answer += 1
    else:
        break
print(answer)