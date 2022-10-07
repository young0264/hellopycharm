import math
M = int(input())
N = int(input())
arr=[]
brr=[]
#if a ** 2 == int(math.sqrt(a)) ** 2:
#    arr.append(a)
#elif b ** 2 == int(math.sqrt(b)) ** 2:
#    arr.append(b)
for i in range(int(math.sqrt(M))+1 ,int(math.sqrt(N))+1):
    brr.append(i**2)
if M==1 :
    brr.append(1)
if brr==[]:
    print(-1)
else:
    print(sum(brr))
    print(min(brr))
