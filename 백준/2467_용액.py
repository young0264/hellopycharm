import sys

n = int(input())
arr = list(map(int,input().split()))
left, right = 0,len(arr)-1
lq,ans_left , ans_right = sys.maxsize,0,0
while left <= right:
    v = abs((arr[left]+arr[right])-0)
    if v<=lq:
        lq = v
        ans_left,ans_right = arr[left],arr[right]
        print("l,r :",arr[left],arr[right])

    if v<0 :
        left += 1
    else: right -= 1
print(left,right,lq)aht


