n = int(input())
arr = []
for _ in range(n):
    x = list(map(str,input().split()))
    arr.append(x)
arr.sort(key = lambda x : (int(x[3]),int(x[2]),int(x[1])))
print(arr[-1][0])
print(arr[0][0])
