import sys
while True:
    n=sys.stdin.readline().rstrip('\n')
    a,b,c,d=0,0,0,0
    if not n:
        break
    for i in n:
        if  97 <= ord(i) <= 122:
            a+=1
        elif 65 <= ord(i) <= 90:
            b+=1
        elif 48 <= ord(i) <= 57 :
            c+=1
        else : d+=1

    print(a,b,c,d)


# input -> try & catch문
#