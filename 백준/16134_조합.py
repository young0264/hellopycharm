def factorial(x):
    sum_value = 1
    while x > 0:
        sum_value *= x
        x = x - 1
    return sum_value

print(factorial(0))

n, r, = map(int, input().split())
m = 1000000007
#answer1 = ((factorial(n)) // (factorial(n - r) * factorial(r))) % m
answer = (factorial(n) % m) * (1 / (factorial(r) * factorial(n - r)) % m)
print(int(answer))
# print(answer1)
