arr=[]
for i in range(3):
    arr.append(input())

if '*' in arr:
    print(int(arr[0])*int(arr[2]))
else:
    print(int(arr[0])+int(arr[2]))