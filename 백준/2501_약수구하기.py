arr=[]
a , b = map(int,input().split())
i=1
while True:
    if a==i:
        arr.append(i)
        break
    elif a % i ==0:
        arr.append(i)
        i+=1
    else:
        i+=1
if b > len(arr):
    print(0)
else: print(arr[b-1])