n, t = map(int,input().split())
arr = list(map(int,input().split()))
brr = [0]*(n-1)

for i in range(n-1):
    x = abs(arr[i]-arr[i+1])
    brr[i] = x
print(brr)
