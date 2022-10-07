# 25 : 쿼터, 10:다임 , 5:니켈, 1:페니
arr = [25,10,5,1]
n = int(input())
for _ in range(n):
    a = int(input())
    res = []
    for i in arr:
        res.append(a//i)
        a = a%i
    print(*res)
