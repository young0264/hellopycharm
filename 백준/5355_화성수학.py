n = int(input())

for i in range(n):
    l = list(map(str,input().split()))
    res=0
    x = float(l[0])
    for j in range(1,len(l)):

        if l[j] =='@':
            x *= 3
        elif l[j] =='%':
            x += 5
        elif l[j] == '#':
            x -= 7
    print('%0.2f'%x)






#ef f(x):
#   if x=='@':
#       return a*3
#   elif x=='%':
#       return a+5
#   else:
#       return a-7



