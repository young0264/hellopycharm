n=int(input())
real=n
for i in range(n):
    arr=input()
    l=len(arr)
    res=[]
    cnt = 1
    res.append(arr[0])
    x = arr[0]

    for j in range(1,l):
        if x == arr[j]:
            cnt+=1
        elif x!=arr[j]:
            if arr[j] not in res:
                res.append(arr[j])
                x = arr[j]
            else:   #다른게 왔는데 res안에 이미 있을경우
                real -= 1
                break

print(real)