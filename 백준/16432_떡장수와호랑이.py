import sys
import time
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
graph = []
for _ in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

answer = []
def dfs(answer_arr,row,exValue): # [],0
    global answer,graph
    for i in range(len(graph[row])):
        if i==0:
            continue

        if graph[row][i] != exValue:
            if row == n-1:
                ans = answer_arr+[graph[row][i] ]
                #print("answer_arr",answer_arr+[i])
                for j in ans:
                    print(j)
                exit(0)
                return answer_arr+[graph[row][i] ]
            else:
                answer += [graph[row][i] ]
                dfs(answer_arr+[graph[row][i] ],row+1,graph[row][i] )
    return False
for i in graph[0][1:]:
    x =  dfs([],0,i)
    if not x:
        print(-1)
        exit(0)







