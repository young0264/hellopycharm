num = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2,1]
a = input()
b = input()
arr = []

for i in range(len(a)):
    arr.append(num[ord(a[i])-65])
    arr.append(num[ord(b[i])-65])
while len(arr)>2:
    for i in range(len(arr)-1):
        arr[i] = ((arr[i]+arr[i+1])%10)
    arr.pop()
arr = list(map(str,arr))
print(''.join(arr))
