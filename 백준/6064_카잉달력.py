# 목표숫자 number , num-x : M으로,,, number-y : N을 기준으로
def f(M,N,x,y):
    num = x
    while num <= M*N:
        if (num-y)%N== 0 :
            return num
        num += M
    return -1
t = int(input())
for _ in range(t):
    M, N, x, y = map(int, input().split())
    num = -1
    i = 0
    res = f(M,N,x,y)
    print(res)
        #elif x%M == 0 :
        #    num = x * i
        #    if num % N == y:
        #        print(num)
        #        break
        #    else : i+=1
        #elif y%N == 0:
        #    num = y * i
        #    if num % M == x:
        #        print(num)
        #        break
        #    else: i += 1
