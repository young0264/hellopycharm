flag = 0
while True:
    s = input()
    flag += 1
    if "-" in s:
        break
    else:
        all = 0
        cnt = 0
        for i in range(len(s)):
            if cnt==0 and s[i]=='}':
                cnt+=1
                all +=1
            elif s[i]=="{":
                cnt +=1
            elif s[i]=="}":
                cnt -=1
        all += cnt//2

        print(str(flag) + ".", all)
