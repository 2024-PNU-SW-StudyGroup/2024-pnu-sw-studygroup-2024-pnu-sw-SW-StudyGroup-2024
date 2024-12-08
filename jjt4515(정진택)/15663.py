n,m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [0] * n
ans = []
def backtracking():
    check = 0   
    if len(ans) == m:
        for n in ans:
            print(n, end=' ')
        print()
        return
    for i in range(len(nums)):
        if check != nums[i] and not visited[i]:
            visited[i] = 1
            ans.append(nums[i])
            check = nums[i]
            backtracking()
            ans.pop()
            visited[i] = 0
            

backtracking()


## 다시 한번 보기