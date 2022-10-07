from collections import deque
n,m=map(int,input().split())
graph = [0 for _ in range(101)]
visited = [0 for _ in range(101)]
for i in range(n+m):    ##graph배열의 사다리와 뱀의 위치에 해당값 넣어주기
    a,b=map(int,input().split())
    graph[a]=b

q = deque()

def bfs(start): #now=1, 1부터 시작
    q.append(start)
    cnt = 0
    while q:
        cnt += 1
        for t in range(len(q)): #주사위 굴린 횟수 구분표시
            node = q.popleft()
            for i in range(1, 7):   #1~6을 이동할 수 있고
                next = node + i
                if graph[next]:     #이동 후 해당위치에 값이있으면(뱀or사다리) 무조건 이동해야함
                    now = graph[next]   #now를 뱀or사다리 값으로 초기화
                else: now = next    #없으면 now를 next만큼 이동
                if 0<=now<101 and visited[now]==0 :#현재위치가 valid 하면
                    q.append(now)
                    visited[now] = True#방문처리를 안하면 뱀이나왔을 경우 같은계산을 반복하게된다
                    if now == 100:  #중지
                        print(cnt)
                        exit(0)
bfs(1)
