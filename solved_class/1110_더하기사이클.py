n=int(input())
x=n
cnt=0
while True:
    a=n//10
    b=n%10
    c=a+b
    n=b*10+c%10
    cnt+=1

    if x==n:
        break
print(cnt)