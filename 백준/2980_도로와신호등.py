n , l = map(int,input().split())
now = 0
time = 0
for _ in range(n):
    d, r, g = map(int,input().split())#위치,빨간불,초록불
    time += d-now
    now = d
    if time % (r+g) <= r :
        time += r - time % (r+g)
time += l-now
print(time)

#현재의 위치와

