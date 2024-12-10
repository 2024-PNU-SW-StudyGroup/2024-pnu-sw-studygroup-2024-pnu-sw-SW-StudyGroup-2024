# 9개의 자연수를 저장할 리스트
numbers = []
for i in range(9):
    num = int(input())
    numbers.append(num)

# 최댓값과 그 인덱스 찾기
max_value = max(numbers)
max_index = numbers.index(max_value) + 1  # 1-based index로 변환

# 결과 출력
print(max_value)
print(max_index)