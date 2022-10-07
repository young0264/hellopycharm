def solution(n):
    answer = ''
    dic ={1:1,2:2,0:4}
    while n:
        answer += str(dic[n%3])
        if n%3:
            n = n//3
        else:
            n= n//3-1
    return answer

print(solution(1)[::-1])