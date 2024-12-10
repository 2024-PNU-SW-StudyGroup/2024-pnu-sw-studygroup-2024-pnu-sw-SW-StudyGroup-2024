# 1. 회의 시작 시간 기준으로 sort한다.
# 2. 회의 시작 시간이 빠른 순서대로 쭉 가다가
# 3. 다음 회의 시작 시간을 만났는데, 다음 회의 종료 시간이 이전 회의 종료 시간보다 뒤에 있으면 무시
import sys

n = int(input())
count = 1
# 회의시간들을 담은 리스트
meetings = []
for _ in range(n):
    meetings.append(list(map(int, sys.stdin.readline().split())))
# 회의시간 정렬
meetings.sort()

start = meetings[0][0]
end = meetings[0][1]

for i in range(1, n):
    if meetings[i][1] <= end:
        if meetings[i][0] == meetings[i][1]:
            if meetings[i][1] == end:
                count+=1
        start = meetings[i][0]
        end = meetings[i][1]
        continue
    if end <= meetings[i][0]:
        count += 1
        start = meetings[i][0]
        end = meetings[i][1]
print(count)




