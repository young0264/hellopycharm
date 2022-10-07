t = int(input())
for _ in range(t):
    j,n = map(int,input().split())
    arr = []
    answer = 0
    sum_value = 0
    for _ in range(n):
        r,c = map(int,input().split())
        arr.append(r*c)
    arr.sort(reverse=True)
    for i in arr:   #12, 10, 10, 9, 8
        j -= i
        answer += 1
        if j<= 0:
            break
    print(answer)



