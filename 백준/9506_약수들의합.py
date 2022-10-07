while True:
    n=int(input())
    arr=[]
    if n == -1:
        break
    for i in range(1,n):
        if n%i==0 :
            arr.append(i)
    res= str(n)+ ' = 1'
    if n != sum(arr):
        print(str(n), 'is NOT perfect.')
    else :
        for i in range(1,len(arr)):
            res += ' + ' + str(arr[i])
        print(res)


