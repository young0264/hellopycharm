def hanoi(n,a,b,c):
    if n==1:
        move.append([a,c])
    else :
        hanoi(n-1,a,c,b)
        move.append([a,c])
        hanoi(n-1,)




move = []