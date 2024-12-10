# 입력 받기
import sys
input = sys.stdin.read
data = input().splitlines()

# 첫 번째 줄에서 n(A), n(B) 읽기
n_a, n_b = map(int, data[0].split())

# 두 번째 줄에서 집합 A 원소 읽기
set_a = set(map(int, data[1].split()))

# 세 번째 줄에서 집합 B 원소 읽기
set_b = set(map(int, data[2].split()))

# 차집합 계산 (A - B)
difference = sorted(set_a - set_b)

# 결과 출력
print(len(difference))
if difference:
    print(" ".join(map(str, difference)))

# 코드 설명: 두 집합 A, B가 주어졌을 때, A - B의 결과를 출력하는 문제입니다. 차집합을 구하는 방법은 set_a - set_b로 간단히 구할 수 있습니다. 차집합을 구한 뒤, 정렬하여 출력하면 됩니다.
# 
# 시간 복잡도는 O(n)입니다.
# 입력 예시

