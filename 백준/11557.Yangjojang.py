t = int(input())
result = []

for i in range(t):
    n=int(input())
    arr = {}
    comp = []
    for j in range(n):
        a,b = map(str,input().split())
        arr[a]=b
        comp.append(int(b))

    for key,value in arr.items():
        if str(max(comp)) == value:
            result.append(key)
for i in result:
    print(i)