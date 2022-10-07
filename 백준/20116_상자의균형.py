m, n = map(int, input().split())
a = list(map(int, input().split()))
result = True
s=0
for i in range(m-1,0,-1):
    s += a[i]
    #if i==0 : result = True
    if a[i-1]-n < s/(m-i) < a[i-1]+n:#
        result = True
    else:
        result = False
        break

if result == True:
    print('stable')
else :
    print('unstable')




