n,a,d = map(int,input().split())
arr= list(map(int,input().split()))ㅂ
answer = 0
now = a
for i in range(n):
    if arr[i] == now:
        answer +=1
        now += d
print(answer)