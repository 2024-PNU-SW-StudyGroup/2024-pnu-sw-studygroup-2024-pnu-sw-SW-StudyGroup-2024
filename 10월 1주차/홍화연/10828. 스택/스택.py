stack = []
result = []

# 명령어 수를 입력받음
N = int(input())

for _ in range(N):
    command = input().strip() # 입력값을 확실히 처리하기 위해 strip() 사용
    
    if command.startswith("push"): # 문자열이 push로 시작되는지 확인
        _, num = command.split() # push는 '_'에, 숫자는 num에 저장
        stack.append(int(num))
    
    elif command == "pop":
        if stack:
            result.append(stack.pop())
        else:
            result.append(-1)
    
    elif command == "size":
        result.append(len(stack))
    
    elif command == "empty":
        if len(stack) != 0:
            result.append(0)
        else:
            result.append(1)
    
    elif command == "top":
        if stack:
            result.append(stack[-1])
        else:    
            result.append(-1)

# 결과 출력
print("\n".join(map(str, result)))