#N , M = map(int,input().split())
#arr = sorted(list(map(int,input().split())))
#result=[]
#def dfs(start,box):
#    if len(box) == M:
#        result.append(box)
#        return
#    for i in range(N):
#        dfs(i+1, box+[arr[i]])
#dfs(0,[])
#for i in result:
#    print(*i)


from itertools import permutations
N , M = map(int,input().split())
arr = sorted(list(map(int,input().split())))
p= list(permutations(arr,M))
for i in p:
    print(*i)