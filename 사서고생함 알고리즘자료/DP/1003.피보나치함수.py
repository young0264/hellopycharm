T=int(input())
arr_0=[0]*41
arr_1=[0]*41


for _ in range(T):
    n=int(input())

    def f_0(n) :
        if  n==1 :
            return 0
        elif n==0 or n==2 :
            return 1
        if arr_0[n] != 0:
            return arr_0[n]
        arr_0[n] = f_0(n-1)+f_0(n-2)
        return arr_0[n]
    #f_0(n) #return?




    def f_1(n) :
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        if arr_1[n] != 0:
            return arr_1[n]
        arr_1[n] = f_1(n-1) + f_1(n-2)
        return arr_1[n]
    #f_1(n)
for i in range(n):
    print(f_0(i), f_1(i))