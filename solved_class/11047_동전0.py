a,b=map(int,input().split())
arr=[]
cnt=0
for _ in range(a):
    x=int(input())
    arr.append(x)
arr.reverse()
#for i in range(a) :
j=0
while True:
    if b%arr[j] !=0 :
        cnt+= b//arr[j] #몫을 cnt에 넣기
        b = b%arr[j]
        j+=1
    else :
        cnt += b // arr[j]
        break

print(cnt)