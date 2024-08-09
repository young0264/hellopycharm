n = int(input())

a1, a2, a3 = list(map(int,input().split()))
b1, b2, b3 = list(map(int,input().split()))
answer = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if (abs(i-a1)>=(n-2) or abs(i-a1)<=2) and(abs(j-a2)>=(n-2) or abs(j-a2)<=2) and (abs(k-a3)>=(n-2) or abs(k-a3)<=2):
                answer += 1
            elif (abs(i-b1)>=(n-2) or abs(i-b1)<=2) and(abs(j-b2)>=(n-2) or abs(j-b2)<=2) and (abs(k-b3)>=(n-2) or abs(k-b3)<=2):
                answer += 1
            # elif abs(i+b1)%n<=2 and abs(j+b2)%n<=2 and abs(k+b3)%n<=2:
print(answer)

