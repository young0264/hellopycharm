def solution(p):
    #u,v 분리하기
    def split2(p):
        # open_p = 0
        # close_p = 0
        #
        # for i in range(len(p)):
        #     if p[i] == '(':
        #         open_p += 1
        #     else:
        #         close_p += 1
        #     if open_p == close_p:
        #         return p[:i + 1], p[i + 1:]
        u,v = '', ''
        cnt = 0
        for i in p:
            if i=='(':
                cnt += 1
                u += '('
            elif i ==')':
                cnt -= 1
                u += ')'
            if cnt == 0:
                length = len(u)
                v = p[length:]
                print("u,v = ",u,v)
                return u, v

    #u가 올바른 문자열인지 판별
    def split3(u):
        cnt = 0
        print("u,cnt : ",u,cnt)
        for i in u:
            if i=='(':
                cnt += 1
            else:   #젠장 반례 u == '))((' : (처음) cnt가 0일떄 False가 리턴되야하지만 -를 수행하는 )가 뒤에나오지 않음
                    #젠장2 반례 u == '()'  : )가 닫히는 시점에 cnt가 0이 되기때문에 False가 리턴. 0미만으로 수정
                    #혹은 cnt ==0 로직 아래에 'cnt -= 1' 을 두어도 됨
                cnt -= 1
                if cnt < 0:
                    return False
        return True

    answer = ''
    # print("p, ans : ",1,p,2,answer)
    if not p:
        return ""

    u,v = split2(p)
    # print("u,v",u,v)
    if split3(u):
        print("u",u,1111111)
        return u + solution(v)

    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        for i in u[1:len(u)-1]:
            # print("u",u[1:-1])
            if i =='(':
                answer += ')'
            else:
                answer += '('
        return answer
# p="(()())()"
p = "()))((()"
print(solution(p))