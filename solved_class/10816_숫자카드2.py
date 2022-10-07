n=int(input())
arr_n=list(map(int,input().split()))
m=int(input())
arr_m=list(map(int,input().split()))
dic={}
for i in arr_n:
    if i in dic:
        dic[i]+=1
    else : dic[i]=1

for i in arr_m:
    if i in dic:
        print(dic[i])
    else : print(0)

#인덱스같은게 숫자가아니라 키가들어가는거지