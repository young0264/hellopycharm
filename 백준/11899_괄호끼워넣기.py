a=0
b=0
s = input()
for i in s:
    if i==')' and a==0:
        b+=1
    elif i=='(':
        a+=1
    elif i==')' and a>0:
        a-=1
print(a+b)