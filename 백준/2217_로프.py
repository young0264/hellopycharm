import sys
input = sys.stdin.readline
n = int(input())
m = sys.maxsize
arr = [int(input()) for _ in range(n)]
arr.sort(reverse = True)
memo =[ i*arr[i-1] for i in range(n,0,-1)]
print(max(memo))
