import sys

# 입력
N = int(sys.stdin.readline())
members = []

for _ in range(N):
    age, name = sys.stdin.readline().split()
    members.append((int(age), name))

# 나이 순으로 정렬 (안정 정렬이므로 입력 순서 유지)
members.sort(key=lambda x: x[0])

# 출력
for member in members:
    sys.stdout.write(f"{member[0]} {member[1]}\n")
