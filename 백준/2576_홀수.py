arr=[]

for i in range(7):
    x = int(input())
    if x%2 ==1:
        arr.append(x)

if arr==[]:
    print(-1)
    exit(0)
print(sum(arr))
print(min(arr))
