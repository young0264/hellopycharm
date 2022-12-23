n=int(input())
f=[0]*(n+1)

for i in range(2,n+1):#n-1번만큼 반복
    f[i]=f[i-1]+1 #f[1]이 뭔지아나?
    if i%2==0:
        f[i] = min(f[i],f[i//2]+1)
    if i%3==0:
        f[i] = min(f[i],f[i//3]+1)



print(f[n])