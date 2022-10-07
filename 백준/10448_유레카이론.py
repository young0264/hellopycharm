#t = int(input())
#arr = []
#for z in range(1,50):
#    arr.append((z*(z+1))//2)
#print(arr)
#for _ in range(t):
#    num = int(input())
#    for i in arr:
#        for j in arr:
#            for k in arr:
#                #exit(0)
#                if i+j+k == num :
#                    print(1)
#




    #print(0)


##아래가 정답코드

def f(list,number):
    for i in list:
        for j in list:
            for k in list:
                if i+j+k == number:
                    return True
    return False##

t = int(input())
arr = []
for z in range(1, 50):
    arr.append((z * (z + 1)) // 2)
for _ in range(t):
    num = int(input())
    if f(arr,num) == True:
        print(1)
    else:
        print(0)