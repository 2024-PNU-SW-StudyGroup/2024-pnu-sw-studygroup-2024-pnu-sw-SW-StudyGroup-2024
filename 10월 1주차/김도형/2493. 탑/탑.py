N = int(input())
lst = list(map(int, input().split()))
answer = []
stack = []

for i in range(len(lst)):
    while stack:
        if stack[-1][1] >= lst[i]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    stack.append((i, lst[i]))
    if len(stack) == 1:
        answer.append(0)
print(' '.join(map(str, answer)))