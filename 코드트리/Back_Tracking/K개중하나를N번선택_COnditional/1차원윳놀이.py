#n번의 턴
#4242
#하나의 숫자가 m이상되면 stop
n,m,k = map(int,input().split())
arr = list(map(int,input().split()))
visited = [0 for _ in range(n)]
pieces = [ 1 for _ in range(k)] #1,1,1
cnt = 0

def calc():
    score = 0
    for piece in pieces:
        if piece >= m :
            score += 1
    return score

def find_max(index):
    global cnt
    cnt = max(cnt,calc())

    if index == n:
        return

    for i in range(k):
        if pieces[i] >= m:
            continue
        pieces[i] += arr[index]
        find_max(index+1)
        pieces[i] -= arr[index]

find_max(0)
print(cnt)


