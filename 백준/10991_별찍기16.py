n = int(input())
for i in range(n):
    print(' '*(n-(i+1)) + ' '.join('*'*(i+1)))