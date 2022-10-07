from collections import deque
import sys
input=lambda: sys.stdin.readline().rstrip()
t=int(input())
for k in range(t):
    l = input()
    b = int(input())
    a = input().rstrip()[1:-1].split(',')
    a = [int(i) for i in a if i]
    arr=deque(a)
    cnt=0
    #'R'일때 reverse를 해주게되면 O(N)의 시간복잡도가 발생하여 시간초과가 나온다.
    # R이나올때를 세어서 홀수일경우에만 한번만 뒤집고 짝수일경우 제자리니까 그대로 진행하도록한다.
    for j in l:
        if j=='R':
            cnt+=1

        elif len(arr) > 0:
            if j=='D':
                if cnt % 2 == 1 :
                    arr.pop()
                else: arr.popleft()
        elif len(arr) == 0:
            if j =='D':

                print('error')
                break
    else:
        if cnt % 2 == 1:
            arr.reverse()

            print(str(list(map(int, arr))).replace(' ',''))
        else:
            print(str(list(map(int, arr))).replace(' ',''))

#빈리스트에서 pop이 일어날 상황이 있으면 예외처리 해줘야함