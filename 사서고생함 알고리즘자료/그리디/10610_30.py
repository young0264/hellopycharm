n=(input())

arr=[ (i) for i in n]

arr.sort()
arr.reverse()
#if
b=int((''.join(arr)))

if b%30==0:
    print(b)
else:
    print(-1)
#print(b)
#print(type(b))