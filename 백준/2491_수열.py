n = int(input())
arr = list(map(int,input().split()))
brr = arr[::-1]
dpa = [0]*n
dpb = [0]*n
dpa[0], dpb[0] = 1,1

for i in range(1,n):
    if arr[i] >= arr[i-1]:
        dpa[i] = dpa[i-1]+1
    else:
        dpa[i] = 1

for i in range(1,n):
    if brr[i] >= brr[i-1]:
        dpb[i] = dpb[i-1]+1
    else:
        dpb[i] = 1
print(max(max(dpa),max(dpb)))