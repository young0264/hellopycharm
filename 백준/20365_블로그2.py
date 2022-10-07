n = int(input())
colors = list(input())
answer = 0
R,B = 0,0
alot = ''
for i in range(n):
    if i == 0:
        if colors[i] == 'R':
            R += 1
        else: B += 1
    else :
        if colors[i] == 'R' and colors[i-1]=='B':
            R +=1
        elif colors[i] =='B' and colors[i-1] =='R':
            B += 1

print(min(R,B)+1)




