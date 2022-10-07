#dfsr개념인 preorder. dictionary개념을 활용하여 간단하게 구현
#딕셔너리의 키를 알파벳,값을 2진트리노드로 두었고 재귀로 방문한 노드(키)값을 리턴하도록 하였다.
#중위순회는 왼쪽->루트>오른쪽을 먼저가야하기에 왼쪽으로 깊이 들어간 후 오른쪽을 리턴하도록 구성하였다.
#후위순회는 왼쪽->오른->루트순으로 리턴

n = int(input())
tree = {}
for _ in range(n):
    node , left, right = list(input().split())
    tree[node] = left, right

def preorder(x):
    if x =='.':
        return
    print(x,end='')
    preorder(tree[x][0])
    preorder(tree[x][1])

def inorder(x):
    if x == '.':
        return
    inorder(tree[x][0])
    print(x,end='')
    inorder(tree[x][1])

def postorder(x):
    if x == '.':
        return
    postorder(tree[x][0])
    postorder(tree[x][1])
    print(x,end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')


