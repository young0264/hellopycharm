arr=[0]*1001
n=int(input())
def f(n):
    if n==1 :
        return 1
    elif n==2 :
        return 2
    if arr[n] != 0:
        return arr[n]
    arr[n]=f(n-1)+f(n-2)
    return arr[n]

#print(arr[n]) ??
print(f(n)%10007)