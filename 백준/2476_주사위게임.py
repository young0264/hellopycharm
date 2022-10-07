# 3개의
n = int(input())
res=[]
for i in range(n):
    arr = [0] * 6
    a, b, c = map(int,input().split())
    arr[a-1] +=1
    arr[b-1] +=1
    arr[c-1] +=1
    if (max(arr)) == 3 :
        res.append((arr.index(3)+1)*1000+10000)
    elif (max(arr))  == 2 :
        res.append((arr.index(2)+1)*100+1000)
    elif (max(arr)) == 1 :
        for i in range(1,7):
            if arr[-i] == 1:
                res.append((7-i)*100)
                break
print(max(res))