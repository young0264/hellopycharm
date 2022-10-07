#39:00

#a[i]=i로 만들기 위한 최소 연산 횟수
#점화식 :
#a[i] = min(a[i-1], a[i/2],a[i/3], a[i/5]) + 1
#* 단 1을 빼는 연산을 제외하고는 해당 수로 나누어 떨어질 때에
#한해 점화식을 적용할 수 있습니다.

x=int(input())
d=[0] * 30001 #3만까지라서

#DP 진행 . bottom up
#가장 적은값에 +1
for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] +1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1 )

print(d[x])