import heapq
import sys
input=sys.stdin.readline
n=int(input())
arr=[]
for i in range(n):
    x=int(input())
    if x>0 :
        heapq.heappush(arr,(-x,x))
    else :  #x가 0일때
        if len(arr)==0:
            print(0)
        else :
            print(heapq.heappop(arr)[1])
