n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
ans = []

for i in range(n):
    x = arr[i]
    ans.append(i+1+x)
print(max(ans)+1)