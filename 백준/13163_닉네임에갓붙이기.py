n = int(input())
name = [list(map(str,input().split())) for i in range(n)]
for i in name:
    print('god'+''.join(i[1:]))