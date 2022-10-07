from math import sqrt
import sys
import time

start = time.time()
input = sys.stdin.readline
n = int(input())
cnt = 0
answer = []

# 이게 에라토스테네스체 # 숫자를 지우는데에 초점
num = [i for i in range(n + 1)]
for i in range(2, int(sqrt(n)+1)):
    if not num[i]: continue #이미 0으로 처리되었으면 지나가
# 2부터 시작하는 i의 배수부터 시작해서 n까지 판별을 완료해줘야
    for j in range(i*i,n+1,i):
        num[j]=False
for i in num:
    if i > 1:
        answer.append(i)

# 이건 소수판별
# def prime_number(x):
#    for i in range(2, int(sqrt(x)) + 1):
#        if not x % i:
#            return False
#    return True
#
#
# if n > 1: answer.append(2)
# for i in range(3, n + 1):
#    if prime_number(i):
#        answer.append(i)
#print(answer)
right = 0
sum_value = 0

for left in range(len(answer)):
    while sum_value < n and right < len(answer):
        sum_value += answer[right]
        right += 1
    if n == sum_value:
        cnt += 1
    sum_value -= answer[left]

end = time.time()
# print("time is : " , end-start)
print(cnt)
