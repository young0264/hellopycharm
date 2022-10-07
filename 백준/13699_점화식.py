n = int(input())
t=[0]*(n+1)
t[0] = 1
def circ(x):
    flag = 0
    for i in range(x):## x==3 >> 0,1,2
        flag += t[i]* t[x-(i+1)]
    t[x] = flag

for i in range(1,n+1):
    circ(i)
print(t[-1])


