n = int(input())
start = 0
end = n
while start <= end:
    mid = (start+end)//2
    if mid**2 >= n:
        end = mid-1
        res = mid
    else :
        start = mid+1
    #print(start, mid, end)
print(res)