import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
sign = input().split()
bool_arr = [False]*10
per_max,per_min = 0,0
#순열이 진행되는 매 순간 해당 부등호를 바로 비교해보게끔. True일때만 진행
#2개부터 비교가능. 1일떄 예외처리
#비교해서 깊이(자리수)가 같아질때 return받아서 max,min을 갱신해준다.
def possible(x,y,s):
    if s =='>':
        if x>y:
            return True
    if s =='<':
        if x<y:
            return True
    return False

def dfs(depth,box):
    global per_max,per_min
    if depth == n+1:
        if not per_min :
            per_min = box
        else: per_max = box
        return
    for i in range(10):
        if not bool_arr[i]:
            if depth == 0 or possible(box[-1],i,sign[depth-1]):
                bool_arr[i] = True
                dfs(depth+1,box+[i])
                bool_arr[i] = False
dfs(0,[])
print(*per_max,sep='')
print(*per_min,sep='')















#selected_min = sys.maxsize
#selected_max = 0
#def dfs(box):
#    if len(box) == n+1:
#        f(box)
#        return
#    for i in range(10):
#        if nums[i] not in box:
#            dfs(box+[nums[i]])
#
#def sign_check(x,y):
#    if x < y :  ##오른쪽이 더클때
#        return True
#    return False    #왼쪽이 더 클때
#res = []
#
#def f(combi):
#    for i in range(n):
#        if sign[i] == '>':
#            if combi[i] < combi[i + 1]:
#                return False
#        if sign[i] == '<':
#            if combi[i] > combi[i + 1]:
#                return False
#    res.append(combi)
#    return
#dfs([])
###############################
#for combi in selected_nums:
#    if f(combi):
#        break
#for combi2 in reversed(selected_nums):
#    if f(combi2):
#        break
#print(len(selected_nums))
#print(*res[-1],sep='')
#print(*res[0],sep='')

