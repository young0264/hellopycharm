#우습지
n = int(input())
arr=[i for i in map(int,input().split())]
   # (input().split())
#arr = [i for i in map(int,input().split())].sort()
arr.sort()

for i in range(1,n):
    arr[i]+=arr[i-1]

print(sum(arr))
#dp?
