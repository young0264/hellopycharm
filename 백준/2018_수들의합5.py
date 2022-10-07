# ㅅㅂ경우의수네
# 15 : 15 // 7,8 // 4,5,6 // 1,2,3,4,5
import sys
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
right =  1
sum_value = 0
cnt = 0

for left in range(1,n+1):
    while sum_value < n and right <= n:
        sum_value += right
        right += 1
    if sum_value == n:
        cnt += 1
        sum_value -= left
    else:
        sum_value -= left

print(cnt)