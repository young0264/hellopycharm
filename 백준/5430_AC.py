from collections import deque

#import json
#s='[1,2,3,4]'
#a=json.loads(s)
#a
#[1,2,3,4]
#type(a) >>> 'list'
t=int(input())
for k in range(t):
    l = input()
    b = int(input())
    a = input().rstrip()[1:-1].split(',')
    a = [int(i) for i in a if i]
    #a=list(map(int,a))
    #print(a)
    arr=deque(a)

    cnt=0
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