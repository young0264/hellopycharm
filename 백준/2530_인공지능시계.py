a,b,c = (map(int,input().split()))
sec=int(input())

h = sec//3600
m = (sec % 3600) // 60
s = (sec % 3600) % 60
a=a+h
b=b+m
c=c+s

#print(a,b,c)
#몫먼저따서 초기화하고,나머지체크
if c >= 60:
    b+= c//60
    c=c%60
if b >= 60:
    a +=(b//60)
    b = b%60
if a  >= 24:
   # a = a//24
    a = a%24

print(a,b,c)