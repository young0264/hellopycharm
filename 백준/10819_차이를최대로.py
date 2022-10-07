from itertools import permutations

def check(x):
    a = 0
    for i in range(n-1):
        a += abs(x[i]-x[i+1])
    return a
def dfs(start,box):
    if len(box) == n:
        res.append(box)
        return
    for i in range(n):
        if arr[i] not in box:
            dfs(start+1,box+[arr[i]])

n = int(input())
arr = list(map(int,(input().split())))
check_max = 0
res = [] #순열담는 리스트

#for i in list(permutations(arr,n)):
#    x = check(i)
#    check_max = max(x,check_max)
#print(check_max)
dfs(0,[])

for i in res:
    #print(i)
    x = check(i)
    check_max = max(x,check_max)
print(check_max)
#print(len(res))
