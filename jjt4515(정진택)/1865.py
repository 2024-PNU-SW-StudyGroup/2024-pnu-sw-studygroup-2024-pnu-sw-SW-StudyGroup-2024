tc = int(input())
    
for _ in range(tc):
    n, m ,w = map(int, input().split())
    edges = []
    for _ in range(m):
        s,e,t = map(int, input().split())
        edges.append([s,e,t])
        if s != e:
            edges.append([e, s, t])
   
    for _ in range(w):
        s,e,t = map(int, input().split())
        edges.append([s, e, -t])
    
    distance = [10001 for _ in range(n+1)]
    distance[1] = 0
    
    ans = 0
    for i in range(1, n+1):
        for j in range(len(edges)):
            s, e, t = edges[j]
            if distance[e] > distance[s] + t:
                distance[e] = distance[s] + t
                if i == n:
                    ans = 1
                    break
                
    
    if ans:
        print("YES")
    else:
        print("NO")
  

