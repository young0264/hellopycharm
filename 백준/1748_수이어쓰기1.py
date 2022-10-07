#arr = []
#n = int(input())
#for i in range(1,n+1):
#    arr.append(str(i))
#x=''
#for i in arr:
#    x += i
#print(len(x))


n = int(input())
ans=[]
def f(x):
    for i in range(9,-1,-1):
        if 10**i <= x <= 10**(i+1)-1:
            cha = (x-(10**i-1))
            res = cha*(i+1)#윗자리수
            ans.append(res)
            f(10**i-1)
f(n)
print(sum(ans))

