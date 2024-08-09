m1,d1, m2,d2 = list(map(int,input().split()))
month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
answer = 0
if m1==m2:
    print(d2-d1+1)
    exit(0)
for i in range(m1+1,m2):
    answer += month_day[i]
answer += month_day[m1]-d1+1
answer += d2
print(answer)

