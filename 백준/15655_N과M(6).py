n , m =map(int,input().split())
arr = sorted(list(map(int,input().split())))
x = arr[0]
def dfs(start,box):     # 함수안에 arr[0]은 안되는건가?
    if len(box) == m :
        print(*box)
        return
    #for i in arr:
    for i in range(start,len(arr)):   #0,1,2
        dfs(i+1,box+[arr[i]])


dfs(0,[])