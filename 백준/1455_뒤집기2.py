#역순으로 진행해도 똒같
#이게 뭐 행에서 하나씪 줄어드나 열에서 하나씩줄어드나 생각할때
# 나에게 맞는 좀 더 단순한것을 기준으로 한번 그려보며 증명을 빨리 해보는것도 좋을 것 같다.
#ㅅ Think simple
r, c = map(int,input().split())
graph = []
answer = 0
for _ in range(r):
    graph.append(list(input()))

def reverse(x,y):
    for i in range(x+1):
        for j in range(y+1):
            if graph[i][j]=="1":
                graph[i][j] = "0"
            else:
                graph[i][j] = "1"
def check(x,y):
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "1":
                return False
    return True

for i in range(r-1,-1,-1):
    for j in range(c-1,-1,-1):
        print("i,j",i,j)
        if graph[i][j] == "1":
            reverse(i,j)
            answer += 1
        if check(i,j):
            print(answer)
            exit(0)
