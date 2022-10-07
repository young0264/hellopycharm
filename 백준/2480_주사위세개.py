# 3개의
arr=[0]*6
a, b, c = map(int,input().split())
arr[a-1] +=1
arr[b-1] +=1
arr[c-1] +=1
if (max(arr)) == 3 :
    print((arr.index(3)+1)*1000+10000)
elif (max(arr))  == 2 :
    print((arr.index(2)+1)*100+1000)
elif (max(arr)) == 1 :
    for i in range(1,7):
        if arr[-i] == 1:
            print((7-i)*100)
            break
