# '.'을 기준으로 구분해서 2번째 인덱스의 값을 카운팅,출력해준다
# 공백을 기준으로 구분되어 있던건
n = int(input())
dic = {}
arr = []
for _ in range(n):
    x = (input().split('.'))
    arr.append(x[1])
    dic[x[1]]=0
    #print(dic)
for i in arr:
    dic[i] +=1
x = sorted( dic.items(), key = lambda x:x[0])
for i in x:
    print(*i)