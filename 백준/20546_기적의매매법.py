cash = int(input())
rate = list(map(int,input().split()))
sungmin = 0 #주식갯수
sungmin_cash = 0    #현금 = 주가*주식갯수
cnt = 0
joon=0
new_cash = cash

for i in range(1,len(rate)-1):    #성민상승
    if rate[i-1] < rate[i]:
        cnt += 1
        if cnt >= 3 :
            sungmin_cash += rate[i]*sungmin
            sungmin = 0
        if rate[i] > rate[i+1]:
            cnt = 0

    elif rate[i-1] > rate[i]:
        cnt -= 1
        if cnt <= -3 :
            sungmin += cash//rate[i]
            cash -= rate[i]*(cash//rate[i])
        elif rate[i] < rate[i+1]:
            cnt = 0

    elif rate[i-1] == rate[i]:
        cnt = 0

    #print(sungmin_cash, sungmin,i, cnt)

for i in range(len(rate)):
    joon += new_cash//rate[i]#준현이 주식개수
    new_cash -= rate[i]*(new_cash//rate[i]) #남은돈 초기화
joon_cash = joon*rate[-1]+new_cash#준현이 14일날 자산

#sungmin_cash += cash
sungmin_cash += (rate[-1]*sungmin+cash)
#print(joon_cash, sungmin_cash)
if joon_cash > sungmin_cash:
    print('BNP')
elif joon_cash < sungmin_cash:
    print('TIMING')
elif joon_cash == sungmin_cash:
    print('SAMESAME')



