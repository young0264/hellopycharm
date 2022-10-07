#def f(n):
#    x , y = 0,1
#    for i in range(0,n):
#        (x,y) = (y,x+y)
#    return x%1000000
#    #b=a+b
#n=int(input())

#N번째 피보나치수를 M으로 나눌 때,
#  M = 10^k (k>2) 이라면, 주기는 항상 15*10^(k-1) 이다.
#- 주기의 길이를 P라고 하면, N번째 피보나치수를 M으로 나눈 나머지는
#    N % M == (N % P) % M
n = int(input())
M= 1000000
P = 1500000 #주기
n=n%P   #이거구나 여기서 시간이 줄어드네
a,b = 0,1
for i in range(n):
    a,b = b%M, (a+b)%M
print(a)