cards = [ i for i in range(1,21)]
for i in range(10):
    a, b = map(int,input().split())
    a= a-1
    flag = cards[a:b]
    cards[a:b] = reversed(flag)

print(*cards)
