##1
polio = list(input())#수정.리스트
for i in range(len(polio)):
    if polio[i]=='X':
        if 0<= i  and i+3 < len(polio) and polio[i:i+4]==['X']*4:
            polio[i:i+4] =  ['A']*4
        elif 0<=i and i+1<len(polio) and polio[i:i+2]==['X']*2:
            polio[i:i+2] = ['B']*2
        else:
            print(-1)
            exit(0)
    else:
        continue
print(''.join(polio))
##2
def polio():
    res = []
    s = input().split('.')
    for i in s:
        if len(i) % 2:
            print(-1)
            return
        res.append('AAAA'*(len(i)//4) + 'BB'*((len(i)%4)//2))
    print('.'.join(res))
polio()
