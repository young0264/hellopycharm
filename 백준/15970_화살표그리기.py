#점들의 색깔은 두가지
#2<=N<=5000
#defaultdict , append// defalt에 set->add, list->append
#아니면 객체 초기화해주고 넣기 / 모양은 둘다 똑같네..
#from collections import defaultdict
#D = defaultdict()
##딕셔너리사용
#n = int(input())
#D = {}
#for _ in range(n):
#    a,b = map(int,input().split())
#    if not b in D:
#        D[b] = [a]
#    else : D[b].append(a)
#D = D.values()
#res = 0
#for i in D:
#    i.sort()
#    if len(i) <= 1:continue
#    res += abs(i[0]-i[1])+abs(i[-1]-i[-2])
#    for j in range(1,len(i)-1):
#        res += min(abs(i[j]-i[j-1]),abs(i[j]-i[j+1]))
#print(res)
##배열
n=int(input())
arr = [[]for _ in range(n)]
for _ in range(n):
    a,b = map(int,input().split())
    arr[b-1].append(a)
res = 0
for i in arr:
    i.sort()
    if len(i) <= 1:continue
    res += abs(i[0]-i[1])+abs(i[-1]-i[-2])
    for j in range(1,len(i)-1):
        res += min(abs(i[j]-i[j-1]),abs(i[j]-i[j+1]))
print(res)


