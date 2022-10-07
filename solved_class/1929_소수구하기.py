m,n=map(int, input().split())
import math
arr=[]


def p_number(x):
    if x<2 :            #2미만으로 설정하는 점
        return False

    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False

    return True


for i in range(m,n+1):
    if(p_number(i)):
        print(i)
