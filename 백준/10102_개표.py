#과반수 출력
res={}

n=int(input())
arr=list(input())
resa=[]
resb=[]

for i in arr:
    if i=='A':
        resa.append(i)
    else :
        resb.append(i)

if len(resa)==len(resb):
    print('Tie')
elif len(resa) > len(resb):
    print('A')
else: print('B')
##reverse_res = dict(map(reversed, res.items()))
#answer=[]
#for key , value in res.items():
#    if  value==(max(res.values())):
#        answer.append(key)
#if len(answer)>1:
#    print('Tie')
#else :
#    print(key)

