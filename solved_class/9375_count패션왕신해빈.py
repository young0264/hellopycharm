from collections import Counter

t = int(input())
for i in range(t):
    n=int(input())
    cloth_type = {}
    cloth=[]
    for j in range(n):
        a,b=input().split()
        cloth.append(b)
        #Counter(cloth)

    result=1
    for k in Counter(cloth):
        result *= Counter(cloth)[k]+1

    print(result-1)

    from collections import Counter

   # a = [1, 2, 3, 1, 2, 2, 3, 1]
   # print(Counter(a))
   # print(Counter(a)[1])
   # for i in Counter(a):
   #     print(i)