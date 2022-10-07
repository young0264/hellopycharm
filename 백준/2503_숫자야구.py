n = int(input())
cnt = 0
arr = []
check = [0]*1000

for i in range(n):
    #arr.append(list(map(int,input().split())))
    num,s,b = map(int,input().split())
    num3 = num%10
    num2 = (num//10)%10
    num1 = (num//100)%10
    for j in range(1000):
        s1,b1=0,0
        j3 = j % 10
        j2 = (j // 10) % 10
        j1 = (j // 100) % 10

        if num1 == j1:  #첫쨰자리
            s1+=1
        elif j1 == num3 or j1== num2:    #
            b1+=1
        if num2 == j2:  #둘쨰자리
            s1+=1
        elif j2 == num1 or j2== num3:
            b1+=1
        if num3 == j3:  #셋째자리
            s1+=1
        elif j3 == num1 or j3==num2:
            b1+=1
        if s1 != s or b1 != b:
            check[j] = 1
        #if not (s1==s and b1==b):
        #    check[j] = 1


for i in range(1000):   #같은자리와,0인것들 초기화해주기
    i3 = i%10
    i2 = (i//10)%10
    i1 = (i//100)%10
    if i1*i2*i3==0 or i1==i2 or i1==i3 or i2==i3 :
        check[i] = 1

print(check.count(0))
