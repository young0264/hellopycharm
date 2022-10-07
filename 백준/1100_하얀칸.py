chess = [input() for _ in range(8)]
#홀수행 홀수열
#짝수행짝수열
res = 0
for i in range(8):
    for j in range(8):
        if i%2==0 and j%2==0 and chess[i][j]=='F':
            res += 1

        elif i%2==1 and j%2==1 and chess[i][j]=='F':
            res+=1
print(res)

