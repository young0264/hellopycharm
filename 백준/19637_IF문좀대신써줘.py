from bisect import bisect_left
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dic = dict()
n_arr = []
s_arr = []
for _ in range(n):
    a,b = map(str,input().split())
    s_arr.append(a)
    n_arr.append(int(b))

for _ in range(m):
    n = int(input())
    idx = -1
    a= bisect_left(n_arr,n)
    print(s_arr[a])
