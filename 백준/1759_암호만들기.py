from itertools import combinations

a , b =map(int,input().split())
l = list(map(str,input().split()))
arr=list(combinations(l,a))
comp=['a' , 'e' , 'i' , 'o' , 'u']
res=[]
for i in arr :  #자음 모음갯수 체크
    za =0
    mo =0
    for j in range(a):
        if i[j] not in comp:
            za+=1
        else:
            mo+=1
    if za>=2 and mo>=1 :
        print(''.join(i))

#res=[]
#for i in arr :
#    x = sorted(i)
#    res.append(x)
#    #print(res)
#    res.sort(key=lambda i: (i[1], i[2], i[3]))
#answer=[]
#comp=['a' , 'e' , 'i' , 'o' , 'u']
#for i in res:
#    cnt=''
#    for j in i:
#        cnt+=j
#    answer.append(cnt)
#answer.sort()
#p =[]
#for i in answer:
#    for j in comp:
#        if not j in i:
#            continue
#        p.append(i)
#print(set(p))
