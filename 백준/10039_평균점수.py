arr=[]
for _ in range(5):
    x = (int(input()))
    if x < 40:
        x=40
    arr.append(x)
res = sum(arr)//5
print(res)