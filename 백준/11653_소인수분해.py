import sys
input = sys.stdin.readline
n=int(input())
cnt = 2

while n:
    if n % cnt == 0:
        n= n//cnt
        print(cnt)
    else :
        cnt +=1
    if n==1 :
        break