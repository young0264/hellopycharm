n, k1 = map(int, input().split())
k2 = 0
num = list(input())
dic = dict()
num2 = sorted(list(map(int, num)))
print(num)
print(num2)

for i in num2:
    if i not in dic:
        dic[i] = 1
        k1 -= 1
    else:
        dic[i] += 1
        k1 -= 1
    if k1 == 0:
        break

print(dic)
