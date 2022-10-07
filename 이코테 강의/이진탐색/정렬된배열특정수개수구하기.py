#정렬후 그 값의 오른쪽인덱스-왼쪽인덱스

from bisect import bisect_left,bisect_right
a,b=map(int, input().split())
arr=list(map(int, input().split()))

def cnt_bisect(x) :
    return bisect_right(arr,x) - bisect_left(arr,x)

if b in arr:
    print(cnt_bisect(b))
else: print(-1)