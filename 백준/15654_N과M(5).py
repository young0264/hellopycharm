
n, m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
pre_list =[0]*n
#box=[]
def dfs(box):
    if len(box) == m :
        print(*box)
        return
    for i in range(n):
        if pre_list[i] == False:
            pre_list[i] = True
            dfs(box+[arr[i]])
            pre_list[i] = False
dfs([])







#permutation을 사용한 풀이
#from itertools import permutations
#N , M = map(int,input().split())
#arr = sorted(list(map(int,input().split())))
#print(arr[1])
#p= list(permutations(arr,M))
#print((p))
#for i in p:
#    print(i)