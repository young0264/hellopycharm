n = int(input())
for _ in range(n):
    a,b = map(list,input().split())
    answer = 0
    cnta , cntb = 0,0
    for i in range(len(a)):
        if a[i]=='1':
            cnta += 1
        if b[i]=='1':
            cntb += 1
    for i in range(len(a)):
        if a[i] != b[i]:
            if cnta == cntb:
                answer += 1/2
            elif cnta > cntb:
                cnta -= 1
                answer += 1
            elif cnta < cntb:
                cntb -= 1
                answer += 1
    print(int(answer))