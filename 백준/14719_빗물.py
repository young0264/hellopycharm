#구현, 해당위치에서 왼쪽max, 오른쪽max탐색후 그 둘중min값이 해당위치에서 담길수 잇는 빗물의양이다.
# 고로 담길수잇는 빗물의양 - 현재위치의블록높이의 차가 빗물이 담길수있는양이 나온다

h , w = map(int,input().split())
block = list(map(int,input().split()))
answer = []
for i in range(1,w-1):
    left = max(block[:i])
    right = max(block[i+1:])
    real = min(left,right)
    rain = real - block[i]
    if rain > 0:
        answer.append(rain)
print(sum(answer))