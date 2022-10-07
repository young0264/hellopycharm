s = input()
answer = 0
now1, now2 = 0, 0
value1, value2 = 0, 0
flag1, flag2 = False, False
for i in s:
    if i == '(' and not flag1:
        flag1 = True
        now1 += 1
    elif i == '[' and not flag2:
        flag2 = True
        now2 += 1

    elif i == ')' and flag1:
        flag1 = False
        now1 -= 1
    elif i == ']' and flag2:
        flag2 = False
        now2 -= 1

    elif i == ')' and not flag1:
        now1 -= 1
    elif i == ']' and not flag2:
        now2 -= 1
