a,b=(map(str,input().split()))
a = ''.join(reversed(a))
b = ''.join(reversed(b))
res = str(int(a)+int(b))
print(int(''.join(reversed(res))))