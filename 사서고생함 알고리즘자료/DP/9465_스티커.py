t=int(input())
#D=[]a
for _ in range(t):
    n=int(input())
    D=[]
    for _ in range(2):
       D.append(list(map(int, input().split()))) #list
    for i in range(1,n): #n-1?
        #if i==0 :
        #    D[0][i] = D[0][0]
        #    D[1][i] = D[1][0]
        if i==1 :
            D[0][i] += D[1][i-1]
            D[1][i] += D[0][i-1]
        else :
            D[0][i] += max(D[1][i-1] , D[1][i-2])
            D[1][i] += max(D[0][i-1] , D[0][i-2])
    print(max(D[0][n-1], D[1][n-1]))

