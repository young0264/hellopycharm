n=list(input())
for i in range(0,len(n),10):
    m=n[i:i+10]
    print(''.join(m))
