l = input().rstrip()

def pelindrom(x):
    for i in range(len(x)//2):
        if x[i] != x[-i-1] :
            return False
    return True    #?

if pelindrom(l): # True이면
    print(len(l))
    exit(0) #이 뭐지

maxl = 0
for i in range(len(l)):
    if pelindrom(l[i:len(l)]): #True이면 # abab일경우에 2가지나옴
        maxl = max(len(l)-i,maxl) #최대비교 max의 반복 초기화
print(maxl + (len(l)-maxl)*2)

