m, n, k = map(int,input().split())
#여성,남성,-인원
team=0
while True:
    if m>=2 and n>=1 and m+n>=k+3:
        m-=2
        n-=1
        team+=1

    else :
        break
print(team)