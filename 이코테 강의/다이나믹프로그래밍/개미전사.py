# 34:00
# a[i] = max(a[i-1], a[i-2] + k[i])
#한칸이상 떨어진 식량창고는 항상 털 수 있으므로
#i-3 번쨰 이해는 고려x
n = int(input())
arr = list(map(int,input().split()))
d=[0]*100
#bottom up 진행
d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2,n):
    d[i] = max(d[i - 1],d[i - 2] + arr[i])

print(d[n - 1])