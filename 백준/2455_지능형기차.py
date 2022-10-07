cnt=0
arr=[]
for i in range(4):
    a , b =map(int,input().split())
    cnt+=b
    cnt-=a
    arr.append(cnt)
print(max(arr))