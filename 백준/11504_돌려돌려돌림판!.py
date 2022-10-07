#X,Y안에 들어가는 M자리의 숫자가 N개로 이루어진 돌림판에서 M자리의숫자와 일차하는 갯수구하기.

T = int(input())
for _ in range(T):
    arr=[]
    cnt = 0
    N,M = map(int,input().split())
    X = int(''.join(list(map(str,input().split()))))
    Y = int(''.join(list(map(str,input().split()))))
    wheel = list(map(str,input().split()))
    wheel = wheel + wheel[:M-1]
    #print(wheel)
    for i in range(N):
        arr.append(wheel[i:i+M])
    for j in range(N):
        arr[j]=int(''.join(arr[j]))
#arr, x, y
    for k in range(N):
        if X <= arr[k] <= Y:
            cnt+=1
    print(cnt)
