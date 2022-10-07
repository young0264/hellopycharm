from itertools import combinations.
n, k = map(int,input().split())
a = [1,2,3]
arr = []
for i in range(1,n+1):
    arr.append(list(combinations(a,i)))
    print(arr)

print(arr)







#import sys
#sys.setrecursionlimit(10**6)
#n, k = map(int,input().split())
#arr = []
#def dfs(box):
#    if sum(box)==n:
#        arr.append(list(box))
#        print(box)
#        return
#
#    for i in range(1,4):
#        dfs(box+[i])
#dfs([])
#print(arr[k])
