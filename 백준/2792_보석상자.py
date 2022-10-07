a,b=map(int,input().split())
arr=[]
#학생은 항상 같은색상의 보석만 가져간다
for i in range(b):
    x=int(input())
    arr.append(x)
if sum(arr)%a == 0:
    print((sum(arr) // a))
else:
    print((sum(arr)//a)+1)
