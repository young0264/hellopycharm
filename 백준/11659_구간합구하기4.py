import sys
#x=sys.stdin.readline()
n , m = map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
#for _ in range(m):
#    a, b = map(int,sys.stdin.readline().split())
#    print(sum(arr[a-1:b]))
for i in range(n-1):
    arr[i+1] +=arr[i] #arr배열에 누적합으로 새로 초기화되는거고
arr = [0]+arr # 0번인덱스를 0으로 넣어주고

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    print(arr[b]-arr[a-1])