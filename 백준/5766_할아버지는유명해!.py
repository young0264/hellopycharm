
while True:
    r,c = map(int,input().split())
    dic = dict()
    if r==0 and c==0:
        break
    max_value = 0
    for i in range(r):
        arr = list(map(int,input().split()))
        for j in arr:
            if j not in dic:
                dic[j] = 1
                max_value = max(max_value,dic[j])
            else:
                dic[j] += 1
                max_value = max(max_value,dic[j])
    num = [[] for _ in range(max_value+1)]
    for i in dic:
        num[dic[i]].append(i)
    cnt = 0
    for i in range(-1,-len(num)-1,-1):
        if num[i] != []:
            cnt +=1
        if cnt ==2:
            x = list(sorted(num[i]))
            print(*x)
            break
