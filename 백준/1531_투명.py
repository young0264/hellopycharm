#1부터 시작한다고 하면 인덱스를 설정할때 0 부터 시작인걸 조심해야한다.

n , m =map(int,input().split())
drawing = [ [0]*100 for _ in range(100) ]

for _  in range(n):
    a1, b1, a2, b2 = map(int,input().split())
    for i in range(b1,b2+1):
        for j in range(a1,a2+1):
            drawing[i-1][j-1] += 1
answer = 0
for i in range(100):
    for j in range(100):
        if drawing[i][j] > m:
            answer += 1
print(answer)

    #for i in range(21,80):
#    for j in range(21,80):
#        drawing[i][j] = 1
#print(drawing[30][32])