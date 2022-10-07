n,m = list(map(int, input().split()))
arr = list(map(int,input().split()))
start=0
end=max(arr)


def cal(mid):
    total = 0
    for i in arr:
        if i > mid :
            total+=i-mid
    return total
while (start<=end):
    mid = (start + end) // 2 #이거하고
    total = cal(mid)              #이게 왜 while문 안에잇어야 꼭하지

    if total >= m :
        start = mid +1
    else:
        end = mid-1
       # result=mid
print(end)
