#1번만 입력받은걸 적으면 되는데
x=[0]*1001
y=[0]*1001
for i in range(3):
    m,n=map(int,input().split())
    x[m] += 1
    y[n] += 1
resx = x.index(1)
resy = y.index(1)
print(resx,resy)