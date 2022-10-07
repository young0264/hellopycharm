from collections import deque
n, w, l=map(int,input().split()) #4 2 8
truck_list = list(map(int,input().split())) #트럭 무게들 리스트
truck=deque()
for i in truck_list:
    truck.append(i)     # 7 4 5 6  #truck덱에 트럭무게들 넣음

cnt=0
arr = deque([0]*(w+1))  # 묶음

while True:
    if len(truck)==1:
        cnt +=w
        break
    else : #입력이 트럭이 여러대

        if sum(arr)<=l:
            arr.append(truck.popleft())
        elif sum(arr)>l:
            truck.appendleft(arr.pop())

            if len(arr)==1:
                cnt += w
            else:
                    cnt+=len(arr)+w-1

        else: #(하중을 넘지 않으면)
            arr.append(truck.popleft())


print(cnt+1)
