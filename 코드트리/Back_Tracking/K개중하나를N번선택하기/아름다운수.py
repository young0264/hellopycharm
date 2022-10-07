import sys
sys.setrecursionlimit(10**6)
n = int(input())
numbers = []
num = [i for i in range(1, 5)]
cnt = 0
def f(box): #백트래킹으로 numbers배열에 조합가능한 n자리수를 담아준다
    global cnt
    if len(box) == n:
        numbers.append(box)
        return
    for i in num:
        f(box + [i])

#1~4사이의 숫자로만 이루어져 있기때문에 숫자별로 아름다운수를 확인하고 초기화해준다
def check(x):
    global cnt
    for i in range(n):
        if x[i] == 1:
            continue
        elif x[i] == 2 and 0<=i and i+1<n:
            if x[i:i+2] == [2]*2:
                x[i:i+2] = [1]*2
            else:return
        elif x[i] == 3 and 0<=i and i+2<n:
            if x[i:i+3] == [3]*3:
                x[i:i+3] = [1]*3
            else:return
        elif x[i] == 4 and 0<=i and i+3<n:
            if x[i:i+4] == [4]*4:
                x[i:i+4] = [1]*4
            else:return
        else:
            return
    cnt += 1
f([])
for i in numbers:   #모든 숫자에 대해서 check하여 cnt값에 변화를 준다.
    check(i)
print(cnt)
###################
# 변수 선언 및 입력:
n = int(input())
ans = 0
seq = list()

def is_beautiful():
    # 연달아 같은 숫자가 나오는 시작 위치를 잡습니다.
    i = 0
    while i < n:
        # 만약 연속하여 해당 숫자만큼 나올 수 없다면
        # 아름다운 수가 아닙니다.
        if i + seq[i] - 1 >= n:
            return False
        # 연속하여 해당 숫자만큼 같은 숫자가 있는지 확인합니다.
        # 하나라도 다른 숫자가 있다면
        # 아름다운 수가 아닙니다.
        for j in range(i, i + seq[i]):
            if seq[j] != seq[i]:
                return False
        i += seq[i]
    return True

def count_beautiful_seq(cnt):
    global ans

    if cnt == n:
        if is_beautiful():
            ans += 1
        return

    for i in range(1, 5):
        seq.append(i)
        count_beautiful_seq(cnt + 1)
        seq.pop()

count_beautiful_seq(0)
print(ans)