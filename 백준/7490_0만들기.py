t = int(input())
arr = [' ', '+', '-']


def cirNum(num):
    res = int(num[0])
    for i in range(1, 2 * n - 1, 2):
        if num[i] == ' ':
            print(num[i-1:i+2])
            print(num[i-1]+num[i+1])
            r = num[i-1]+num[i+1]
            num[i-1:i+2] = r


            print("n",num)
    for i in range(1, len(num)):
        if num[i] == '+':
            res += int(num[i+1])
        elif num[i] == '-':
            res -= int(num[i+1])
    # print("res",res)
    if res==0:
        return True
    else:
        return False

import sys
def input():
    return sys.stdin.readline().rstrip()
def dfs(num,box):
    if num==n+1:
        new_box = box.replace(' ','')
        r = eval(new_box)
        if r==0:
            answer.append(box)
        return
    for a in arr:
        dfs(num+1, box+a+str(num))

answer = []
for _ in range(t):
    n = int(input())
    dfs(2,'1')
    answer.append(' ')
print(*answer,sep='\n')

# def dfs(num):  # cnt 0부터
#     if len(box)>=2*n+1:
#         return
#     if num==n+1:
#     # if len(box)==2*n-1:
#         print("box",box)
#         return
#
#     box.append(num)
#     for i in range(3):
#         box.append(arr[i])
#         dfs(num + 1)
#         box.pop()
#
# for _ in range(t):
#     n = int(input())
#     box = []
#     dfs(1)
#
