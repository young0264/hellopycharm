n=int(input())
arr = list(map(int,input().split()))
ha = len(arr)//2
if len(arr)%2 == 0 :
    arr.sort()
    arr.reverse()
    print(sum(arr[0:ha])*2)

else:
    arr.sort()
    arr.reverse()
    print(sum(arr[0:ha]*2)+arr[ha])