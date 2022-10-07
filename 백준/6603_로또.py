def dfs(start, box):
    if len(box) == 6:
        print(*box)
        return
    for i in range(start, k):
        dfs(i + 1, box + [arr[i]])
        #if not visited[i]:
        #    visited[i] = True
        #    visited[i] = 0

while True:
    arr = list(map(int,input().split()))
    visited = [0]*(arr[0])
    if arr == [0] :
        break
    k = arr[0]
    arr = arr[1:]
    dfs(0,[])
    print()
