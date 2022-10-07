import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [0]*(n+1)
for _ in range(m):
    bookNum = int(input())
    books = list(map(int, input().split()))
    for i in range(len(books)):
        arr[books[-i-1]] = i+1
print(arr)
for i in range(1,n):
    print(i)
    if arr[i] > arr[i+1]:
        print("No")
        exit(0)
print("Yes")

