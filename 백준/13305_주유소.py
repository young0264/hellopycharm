#도시의개수n,
#도로의길이n-1개
#각 도시의 주유소에서 리터당가격
#앞의 주유소 min값을 갱신하여 그걸로 매 거리의 값을 사는거야.
n = int(input())
dist = list(map(int,input().split()))
price = list(map(int,input().split()))
min_value = price[0]
res = 0
for i in range(n-1):
    min_value = min(min_value,price[i])
    res += dist[i]*min_value
print(res)