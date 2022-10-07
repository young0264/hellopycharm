def f(n):
    x,y=0,1
    for i in range(0,n):
        y=x+y
        x=y
        #x,y =y, x + y

    return x
x=int(input())
print(f(x))