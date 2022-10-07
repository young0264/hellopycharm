from itertools import combinations
arr=[]
for i in range(9):
    arr.append(int(input()))
result = list(combinations(arr,7))
answer=[]
for i in result:
    if sum(i) == 100:
        answer.append(i)
if len(answer) ==1:
    for i in sorted(answer[0]):
        print(i)
else :
    for i in sorted(answer[0]):
        print(i)







#res=0
#arr=[]
#for i in range(9):
#    n=int(input())
#    arr.append(n)
#xa = sum(arr)-100
#any=0
#for i in arr:
#    for j in arr:
#        if i == j :
#            continue ######
#        elif i+j==xa:
#            arr.remove(i)
#            arr.remove(j)
#        if len(arr)==7:     #이거 설정 안해주면 remove상태에서 7개로 돌면서 값찾게됨
#            break
#arr.sort()
#for i in arr:
#    print(i)
###########
#이거.9C7 arr에 넣고 if sum==100 for문으로 arr출력