n = int(input())
edges = [[] for _ in range(n+1)] 
for _ in range(n):
    mid, left, right = map(str, input().split())
    mid = ord(mid) - 64
    if left != '.':
        left = ord(left) - 64
    else:
        left = 0
    if right != '.':
        right = ord(right) - 64
    else:
        right = 0
    edges[mid].append(left)
    edges[mid].append(right)

def preOrder(node):
    if node == 0:
        return
    print(chr(node+64), end="")
    preOrder(edges[node][0])
    preOrder(edges[node][1])

def inOrder(node):
    if node == 0:
        return
    inOrder(edges[node][0])
    print(chr(node+64), end="")
    inOrder(edges[node][1])

def postOrder(node):
    if node == 0:
        return
    postOrder(edges[node][0])
    postOrder(edges[node][1])
    print(chr(node+64), end="")

preOrder(1)
print()
inOrder(1)
print()
postOrder(1)
