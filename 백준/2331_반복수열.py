#반복되는걸 찾아야하고>>>>
#반복되는부분 제외
#같은숫자가 나오는순간을 찾으면 되고 >> 처음부터 같은숫자 전까지의 갯수가 정답!
#문제조건에서 5자리까지 고려해줘야함
a , b = map(int,input().split())
arr=[a]
i=0
while True :

    a5 = a % 10
    a4 = (a // 10) % 10
    a3 = (a // 100) % 10
    a2 = (a // 1000) % 10
    a1 = (a // 10000) % 10
    x = a1**b + a2**b + a3**b + a4**b +a5**b
    a = x
    #print(arr)
    if x in arr:
        i = arr.index(x)
        print(i)
        break
    arr.append(x)

