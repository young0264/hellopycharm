def combinations(arr,n):
    result = []

    if n==0 :
        return[[]]

    for i in range(0, len(arr)):
        element = arr[i]
        rest_arr = arr[i+1:]
        for C in combinations(rest_arr, n-1):
            result.append([element]+C)

    return result



#def combine(self, n:int, k:int) -> List[List[int]]:
#    results = []
#
#    def dfs(elements, start: int, k:int):
#        if k == 0:
#            results.append(elements[:])
#            return
#
#        for i in range(start, n + 1):
#            elements.append(i)
#            dfs(elements, i + 1, k - 1)
#            elements.pop()
#    dfs([], 1, k)
#    return results
#
########
#def dfs(arr,n):
#    result = []
#    if n==0:
#        return[[]]
#    for i in range(len(arr)):
#        element = arr[i]
#        rest_arr = arr[i+1:]
#        for k in dfs(rest_arr,n-1):
#            result.append()

#l = [1,2,3,4]
#n = len(l)
#r = 3
#answer = []
#
#def dfs(idx, list):
#    if len(list) == r:
#        answer.append(list[:])
#        return
#    for i in range(idx, n): #idx가 1씩증가할꺼
#        dfs(i+1, list.append(l[i]))   #list+[l[i]]
#dfs(0,[])
#print(answer)
########책 내용
#def combine(self,n,k):
#    results = []
#    def dfs(elements,start:int, k:int):
#        if k ==0 :
#            results.append(elements[:])
#            return
#        for i in range(start,n+1):
#            elements.append(i)
#            dfs(elements, i+1,k-1)
#            elements.pop()
#    dfs([],1,k)
#    return results
#print(combine(l,2,1))

########
n , k = 4 , 2      # ex1)>>>>>[1,2],[1,3],[1,4,[2,3],[2,4],[3,4]
                   # ex2) n=1, k=1 : >>>> [[1]]
def combine(self, n, k):
    result=[]
    def dfs(index,path):
        if len(path) == k:
            result.append(path)
            return
        for i in range(index)

#######
result = []
n = 4  # 4개중
k = 2  # 2개뽑기


def dfs(start, path):
    print(path)
    print(result)
    if len(path) == k:  # 만약 path의 빈배열이 완성이(정상적으로 뽑히면) 되면 result에 넣어주고
        result.append(path)
        return
    for i in range(start, n + 1):  # 1부터시작해서 #[1,2,3,4] 1부터뽑아주고.
        dfs(i + 1, path + [i])  # start+=1 , path += 첫째자리


dfs(1, [])
print(result)

