n=int(input())
a=1
for i in range(2, n+1):
    a *=i
#a=팩토리얼값
a=list(str(a))
cnt=0
#for j in range(1,len(a)+1):
#0이 아닌게 나올때 stop하기..
j=0
while True :
    if a[::-1][j]=='0' :
        cnt+=1
        j+=1
    else :
        break
print(cnt)
