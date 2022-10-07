t = int(input())
for i in range(t):
    n = int(input())
    dic = {}
    for j in range(n):
        arr = list(map(str,input().split()))
        dic[int(arr[0])]= arr[1]
    print(dic[max(dic)])

