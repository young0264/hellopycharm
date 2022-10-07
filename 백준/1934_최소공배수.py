n=int(input())
def gcd(a,b): #a,b의 최대공약수를 먼저 구해보자
    while b:
        a,b = b,a%b
    return a


for i in range(n):
    a,b=map(int,input().split())
    arr=[]
    print(a*b//gcd(a,b))







#import sys
#input = sys.stdin.readline
#n=int(input())
#for i in range(n):
#    a, b = map(int,input().split())
#    x = max(a,b)    #공배수가 될 미지수x
#    while True:     #두숫자 모두로다 나눠지는 그 순간
#        if (x%a,x%b)==(0,0):
#            print(x)
#            break
#        else:
#            x += 1