from collections import defaultdict

# 테스트 케이스 수 입력
t = int(input())

for _ in range(t):
    n = int(input())  # 의상 수
    clothes = defaultdict(list)  # 의상 종류별 저장

    # 의상 입력 처리
    for _ in range(n):
        name, category = input().split()
        clothes[category].append(name)

    # 경우의 수 계산
    total_combinations = 1
    for category in clothes:
        total_combinations *= (len(clothes[category]) + 1)

    # 알몸인 상태(모두 선택하지 않은 경우) 제외
    print(total_combinations - 1)
