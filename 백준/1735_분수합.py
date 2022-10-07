arr=[]
for i in range(2):
    a=list(map(int,input().split()))
    arr.append(a)
a = arr[0][0]*arr[1][1] + arr[0][1]*arr[1][0]
b = arr[0][1]*arr[1][1]
print(a,b)