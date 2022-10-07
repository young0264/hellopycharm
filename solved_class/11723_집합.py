import sys
s=set()

n=int(input())
for i in range(n):
    x = sys.stdin.readline().rstrip().split()
    #y = int(x[1])
    if len(x)==1:
        if   x[0] == 'all' :
            s = {i for i in range(1,21)}
            continue
        else :
            s = set()
    else:

        if x[0] =='add':
            s.add(int(x[1]))
        elif x[0] == 'remove':
            if int(x[1]) in s:
                s.discard(int(x[1]))

        elif x[0] == 'check' :
            if int(x[1]) in s:
                print(1)
            else: print(0)
        elif x[0] == 'toggle' :
            if int(x[1]) in s:
                s.remove(int(x[1]))
            else: s.add(int(x[1]))

#discard를 안하고 remove를해야 답이 나오네..




