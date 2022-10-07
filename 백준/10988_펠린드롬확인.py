l = input()
ll = len(l)
f=0
if ll == 1:
    print(1)
    exit(0)
for i in range(ll//2):
    if l[i]!=l[ll-1-i]:
        print(0)
        exit(0)
    else:
        print(1)
if f==True:
    print(1)