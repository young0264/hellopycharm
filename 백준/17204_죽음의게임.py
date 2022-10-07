n , k = map(int,input().split())
number = [ int(input()) for _ in range(n)]
arr = []
flag = 0
cnt = 0
for i in range(n):
    flag = number[flag]
    cnt += 1
    if flag == k:
        print(cnt)
        exit(0)
print(-1)

#양의 정수 M을 외친다.
#같은 방식으로 반복해 M까지 말하게 된다.
#문젲같네