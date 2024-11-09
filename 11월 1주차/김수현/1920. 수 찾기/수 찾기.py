def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left+right) // 2
        if array[mid] == target:
            return 1
        if array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 0

n = int(input())
array = sorted(list(map(int, input().split())))
m = int(input())
num = list(map(int, input().split()))
for i in range(m):
    print(binary_search(array, num[i]))