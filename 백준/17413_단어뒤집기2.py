arr = input()
res = '' ##ans에 넣을모양
res1 = ''##리버스해서 res에 넣을모양
flag = 0
for j in arr:

    if j == '<':
        flag += 1
        if not res1 =='': res += ''.join(list(reversed(res1)))
        res1 = ''
    elif j == '>' : flag -= 1

    if flag%2 == 1: ##<>안쪽
        res += j
    elif flag%2 == 0 :
        if j == ' ':
            res += ''.join(list(reversed(res1)))
            res += ' '
            res1 = ''
        elif j == '>':
            res += j
        else:
            res1 += j
if not res1=='':
    res += ''.join(list(reversed(res1)))
print(res)