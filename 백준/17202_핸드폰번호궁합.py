a = list(map(int,list(input())))
b = list(map(int,list(input())))
arr =[]
for i in range(len(a)):
    arr.append(a[i])
    arr.append(b[i])
flag = len(arr)
while flag>2 :
    for i in range(len(arr)-1):
        arr[i] = (arr[i]+arr[i+1])%10
    arr.pop()
    flag -= 1

arr = list(map(str,arr))
print(''.join(arr))