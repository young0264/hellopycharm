#temp
n , t = map(int,input().split())   # 2*n개 두줄로 , t초후
up = list(map(int,input().split()))
down = list(map(int,input().split()))
up.extend(down)
for i in range(t):
    temp = up[-1]
    up[1:2*n]= up[0:2*n-1]
    up[0] = temp
print(*up[0:n])
print(*up[n:2*n])

#혹시 슬라이싱으로 문제를 해결하면 시간복잡도? 성능면에서
#그리고 배열에 저구