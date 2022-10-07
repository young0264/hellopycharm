n=int(input())
arr=list(map(int,input().split()))
d=[1]*(n)

for i in range(1,n):
    for j in range(i):
        if arr[i]>arr[j]:
            d[i]=max(d[i],d[j]+1)# 후.

print(max(d))




#n=int(input())
#arr=list(map(int,input().split()))
#k=0
#cnt=1
#d=[1 ]*1001
#for num in range(1,n):
#    for i in range(num,n):
#        if arr[k] < arr[i]:
#            arr[k]=arr[i]
#            cnt+=1

#print(cnt)


