#중복을 피하기위해(되돌아가는 경우가 있으니) arr배열을 만들어 방문처리를 해준다
#각 경우에맞춰
#숫자를 기준으로 연산하기
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())


#def bfs():
#    q = deque()
#    q.append([a,""])    #int형
#    while q:
#        num,box = q.popleft()   #box에 알파벳저장
#        nd = (num*2)%10000
#        if nd == b:   return box+'D'
#        elif arr[nd]==0:
#            arr[nd] = 1
#            q.append([nd,box+"D"])
#
#        ns = ((num-1)+10000)%10000
#        if ns == b:return box+'S'
#        elif arr[ns] == 0:
#            arr[ns] = 1
#            q.append([ns,box+"S"])
#        nl = ((num%1000)*10)+(num//1000)
#        if nl == b: return box+'L'
#        elif arr[nl] == 0:
#            arr[nl] = 1
#            q.append([nl,box+"L"])
#
#        nr = (num%10)*1000+num//10
#        if nr == b: return box+'R'
#        elif arr[nr] == 0:
#            arr[nr] = 1
#            q.append([nr,box+"R"])



def bfs():
    q = deque()
    q.append((a,""))
    while q:
        num,box = q.popleft()   #box에 알파벳저장
        nd = str((int(num)*2)%10000)
        if int(nd) == int(b):
            print(box+'D')
            return
        elif arr[int(nd)]==0:
            arr[int(nd)] = 1
            q.append((nd,box+"D"))

        ns = str(((int(num)-1)+10000)%10000)
        if int(ns) == int(b):
            print(box+'S')
            return
        elif arr[int(ns)] == 0:
            arr[int(ns)] = 1
            q.append((ns,box+"S"))

        nl = num[1:]+num[0]
        if int(nl) == int(b):
            print(box+'L')
            return
        elif arr[int(nl)] == 0:
            arr[int(nl)] = 1
            q.append((nl,box+"L"))

        nr = num[-1]+num[:-1]
        if int(nr) == int(b):
            print(box+'R')
            return
        elif arr[int(nr)] == 0:
            arr[int(nr)] = 1
            q.append((nr,box+"R"))
for _ in range(n):
    a,b = map(str,input().split())
    arr = [0]*10000
    bfs()
