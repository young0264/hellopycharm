n = int(input())
for i in range(n):
    if (i+1)%2==0:
        print(' '+' '.join('*'*n))
    else: print(' '.join('*'*n))