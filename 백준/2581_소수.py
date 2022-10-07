import math
def primenumber(x):
    if x == 1: return False
    if x == 2: return True
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False    #  안나눠져야 소수
    return True     # 이게 소수

arr=[]
m=int(input())
n=int(input())
for i in range(m,n+1):
    if primenumber(i) == True:
        arr.append(i)
if len(arr)==0:
    print(-1)
    exit(0)
print(sum(arr))
print(min(arr))