def solution(s, t):
    for _ in range(len(t) - len(s)):
        if t[-1] == 'A':
            t = t[:-1]
        else:
            t = t[:-1]
            t = t[::-1]

    return 1 if s == t else 0


S = input()
T = input()

print(solution(S, T))