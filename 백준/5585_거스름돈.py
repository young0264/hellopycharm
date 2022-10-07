import sys
input = sys.stdin.readline
n = int(input())
#a,b,c,d,e,f 500 100 50 10 5 1
arr = [500,100,50,10,5,1]
ans = 0
money = 1000 - n
for i in arr:
    a = money//i
    ans += a
    money = money%i
print(ans)




#ans = 0
#money = 1000 - n
#ans += money//500
#a = money - money//500
#ans += money//100