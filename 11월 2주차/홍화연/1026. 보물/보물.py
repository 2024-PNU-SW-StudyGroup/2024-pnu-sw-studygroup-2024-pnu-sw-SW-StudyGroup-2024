# 입력 받기
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# A는 오름차순, B는 내림차순으로 정렬
a.sort()
b.sort(reverse=True)

# S 계산
s = sum(a[i] * b[i] for i in range(n))

# 결과 출력
print(s)

# 설명: 

