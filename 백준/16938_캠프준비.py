from itertools import combinations
n,l,r,x = map(int,input().split())
arr = list(map(int,input().split()))
# visited = [0]*n
box = []
answer = 0
# s = set()
# dic = dict()
def problem_level(b):
    return l <= sum(b) <= r

def min_max_value(b):
    return x <= (max(b) - min(b))

def dfs(idx):
    global answer
    # print(box)
    if len(box)>1 and problem_level(box) and min_max_value(box):#계속 진행해야해.
        answer += 1

    if sum(box)>r: #리턴해줄 조건을 맞들어줘야해 , r은 sum(arr)보다는 작을테니.
        return

    for i in range(idx,n):
        box.append(arr[i])
        dfs(i+1)
        box.pop()

dfs(0)

# for i in range(2,n+1):
#     for combi in combinations(arr,i):
#         # print("combi",combi)
#         if problem_level(combi) and min_max_value(combi):
#             answer += 1

print(answer)
