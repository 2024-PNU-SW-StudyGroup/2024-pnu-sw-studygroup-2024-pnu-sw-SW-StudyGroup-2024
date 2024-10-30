n=input()
n=int(n)
k=n-1
for i in range(1, n+1):
    print((' '*k)+('*'*i))
    k-=1

