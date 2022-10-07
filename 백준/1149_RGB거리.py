n=int(input())
d=[]
for i in range(n):
    x= list(map(int,input().split()))
    d.append(x)

for i in range(1,n):    #빨초파
    d[i][0]=min(d[i-1][1],d[i-1][2])+d[i][0]
    d[i][1]=min(d[i-1][0],d[i-1][2])+d[i][1]
    d[i][2]=min(d[i-1][0],d[i-1][1])+d[i][2]

print(min(d[n-1][0],d[n-1][1],d[n-1][2]))

