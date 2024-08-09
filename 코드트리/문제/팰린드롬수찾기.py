x,y = map(int,input().split())

def is_pelin(num):
    str_num = str(num)
    n = len(str_num)
    flag = 1
    for i in range(n):
        if str_num[i] != str_num[-i-1]:
            flag = 0
            break
    if flag:
        return True
    return False
answer = 0
for n in range(x,y+1):
    res = is_pelin(n)
    if res:
        answer += 1
print(answer)