t = int(input())
arr= []
for _ in range(t):
    n = int(input())
    arr.append(n)
arr.sort(reverse=True)
c = 0
for i in range(2,len(arr),3):
    c+=arr[i]
print(sum(arr)-c)
