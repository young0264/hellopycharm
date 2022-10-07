import sys
def input():
    return sys.stdin.readline().rstrip()
#값에대한 idx를 찾는것이 아닌 값에대해 모든 arr를 돌면서 몫cnt를 m개와 비교를해서
# cnt가 m보다 크면 숫자를 높여야하므로 left초기화 반대는 right초기화를 한다
# cnt가 m보다 작은경우에는 해당사항이 아니므로 answer를 초기화하지 않는다.
m, n = map(int, input().split())
arr = list(sorted(map(int, input().split())))
left, right = 0, arr[-1]
answer = 0

while left <= right:
    mid = (left+right)//2
    cnt = 0
    if mid==0:
        print(0)
        exit(0)
    for i in range(n):
        cnt += (arr[i]//mid)

    if cnt >= m:
        left = mid + 1
        answer = mid
    else:
        right = mid -1

print(answer)
