def solution(s):
    answer = 0
    length = len(s)
    flag = False
    cnt_arr = []
    ans_arr = []
    for i in range(length):
        cnt = 1
        res = ''
        x = s[:i+1]
        print("x",x)

        for j in range(i, length):
            if x == s[j:j+i+1]:   #문자가 같으면
                cnt += 1
            else:           #다를때 멈출때
                if cnt == 1 :
                    res += x
                else:
                    res += (str(cnt) + x)
                cnt = 1
                x = s[j:j+i+1]

        if cnt == 1:
            res += x
        else:
            res += str(cnt) + x

    return ans_arr

s="abcabcdede"
s="abcabcabcabcdededededede"#여기16
s="ababcdcdababcdcd"
s="ababcdcdababcdcd"   ##여기18
s="abcabcabcabcdededededede"
s="xababcdcdababcdcd"
s="aabbaccc"    #8
print(solution(s))
