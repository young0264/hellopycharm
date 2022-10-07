# 가장 인접한 두 공유기 사이의 거리가 최대가 되게하려면
# c개를 설치해서.

n, c = map(int, input().split())
house = []
dist = []
for _ in range(n):
    house.append(int(input()))
house.sort()
left, right = 1, house[-1] - house[0],
answer = 0

if c == 2:
    print(right)
    exit(0)
while (left <= right):
    mid = (left + right) // 2
    cnt = 1
    pos = 0
    for i in range(n):
        if house[i] - house[pos] >= mid:
            pos = i
            cnt += 1
    if cnt >= c:
        left = mid+1
        answer = mid
    else:
        right = mid-1
print(answer)
# for i in range(n):
#    for j in range(n):
#        d = house[i + 1] - house[i]
#    dist.append(d)
# dist = list(set(dist))

# now = 0
# max_answer = 0
# for d in dist:
#    max_dist=0
#    cnt = 1
#    pos = 0
#    for j in range(1,n):
#        x = house[j] - house[pos]
#        if x >= d:
#            max_dist = max(max_dist,x)
#            pos = j
#            cnt += 1
#        else: continue
#        if cnt == c:
#            print(max_dist)
#
# print("dist : ", dist)
