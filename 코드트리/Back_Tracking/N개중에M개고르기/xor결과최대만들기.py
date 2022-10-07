n,m = map(int,input().split())
numbers = list(map(int,input().split()))
max_value = 0
def dfs(start,box,nums):
    global max_value#,cnt_value
    if len(box) == m:
        max_value = max(max_value,nums)
        return
    for i in range(start,n):
        dfs(i+1,box+[1],nums^numbers[i])
dfs(0,[],0)
print(max_value)