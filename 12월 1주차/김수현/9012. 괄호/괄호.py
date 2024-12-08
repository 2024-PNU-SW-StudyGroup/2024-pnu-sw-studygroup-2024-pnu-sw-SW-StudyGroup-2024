t = int(input())
for i in range(t):
    s = input()
    stack = []
    for j in range(0,len(s)):
        if len(stack) == 0:
            stack.append(s[j])
        else:
            if stack[-1]+s[j] == '()':
                stack.pop()
            else:
                stack.append(s[j])
    if len(stack) == 0 :
        print('YES')
    else:
        print('NO')