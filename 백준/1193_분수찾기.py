n=int(input())
i=1
x=(i*(i+1))//2
da=i*(i-1)//2
while n:
    if da < n <= x:
        i+=1
    else :
        break
    result = n - i*(i-1)/2
    print(f"{result}/ {i-result}")