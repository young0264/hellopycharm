import heapq, sys

input = sys.stdin.readline
t = int(input())
arr=[]

for i in range(t):
    x = int(input())
    if x != 0 :
        heapq.heappush(arr,(abs(x),x))
    else : #x가 0일때
        if len(arr)==0 :
            print(0)
        else :
            print(heapq.heappop(arr)[1])