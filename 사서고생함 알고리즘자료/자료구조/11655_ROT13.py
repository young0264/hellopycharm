n=list(input())

for i in range(len(n)) :
    if n[i].isupper() :
        if ord(n[i])+13 <= 90 :
            n[i]=chr(ord(n[i])+13)
        elif ord(n[i])+13 >= 90 :
            n[i]=chr(ord(n[i])-13)
    if n[i].islower() :
        if ord(n[i]) +13 <=122:
            n[i]=chr(ord(n[i])+13)
        elif ord(n[i]) +13 >122:
            n[i]=chr(ord(n[i])-13)

print(''.join(n))
