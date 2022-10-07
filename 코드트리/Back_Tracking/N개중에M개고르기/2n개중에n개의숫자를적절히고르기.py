#이거 어디서 본건데.스타크
import sys
sys.setrecursionlimit(10**6)
n = int(input())
arr = list(map(int,input().split()))
combination_nums = []
def dfs(start,box):
    if len(box) == n:
        combination_nums.append(box)
        return
    for i in range(start,2*n):
        dfs(i+1 ,box+[arr[i]])
dfs(0,[])
ans = sys.maxsize
for i in combination_nums:
    another_nums = abs(sum(arr)-2*sum(i))
    ans = min(ans,another_nums)
print(ans)