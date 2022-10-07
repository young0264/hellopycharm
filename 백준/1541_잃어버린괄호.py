n = input()
answer = 0 #정답 축척공간
now = '' #문자형 숫자를 담을 공간
dir = 0 #짝수 -> 양수, 홀수 -> 음수
for i in n :
    if i == '+':    #+일때에는 dir에 따라서 answer값을 변경시켜줌
        if dir%2 == 0:
            answer += int(now)
            now = ''
        else:
            answer -= int(now)
            now = ''
    elif i =='-':   #-일때에는 dir이 짝수일때만 홀수로 바꿔줘
        if dir%2 == 0:
            answer += int(now)
            now = ''
            dir += 1
        else:       #-일때 dir은 유지
            answer -= int(now)
            now = ''
    else:
        now += i
if dir%2 == 0:      #마지막 숫자를 계산하기위해 dir에 따라서 answer에 값을 더해줘
    answer += int(now)
else:
    answer -= int(now)

print(answer)#마지막 숫자까지 더해주면 출력
