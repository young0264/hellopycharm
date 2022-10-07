#하나씩 따져야할 인자를 for문으로 받은거


n = int(input())
arr = [[0]*1000 for _ in range(1000)]
dir_num = 0
dx = [1,-1,0,0]
dy = [0,0,-1,1] #동서남북순으로
x,y = 0,0
cnt = 0
ans = -1
def move(map,len) : #동서남북 , 가는 거리
    global x,y,cnt,ans
    for i in range(len):
        if map == 'E':
            x = x+dx[0]
            y = y+dy[0]
            cnt += 1
        elif map == 'W':
            x = x + dx[1]
            y = y + dy[1]
            cnt +=1
        elif map == 'S':
            x = x + dx[2]
            y = y + dy[2]
            cnt +=1
        else:
            x = x + dx[3]
            y = y + dy[3]
            cnt +=1
        if x == 0 and y == 0 :
            ans = cnt
            return True
    return False
for _ in range(n) :
    a , b = map(str,input().split())
    if move(a, int(b)) == True :
        print(ans)
        exit(0)
print(-1)












# mapper = {
#    'E':0,
#    'W':1,
#    'S':2,
#    'N':3
# }
# cnt = 0
#for _ in range(n):
#    a, b = map(str, input().split())  # a가 방향,b가 횟수
#    x = x + dx[mapper[a]]*int(b)
#    y = y + dy[mapper[a]]*int(b)
#    cnt += 1*int(b)
##    if (x,y) == (0,0):
#print(x,y)





