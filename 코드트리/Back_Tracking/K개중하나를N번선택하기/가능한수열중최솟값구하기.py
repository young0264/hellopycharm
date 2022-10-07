import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
#1글자 : 4출력
#2글자 : 45
#3글자 : 454
#4글자부터는 입력받는 i
#1: arr[-1]와 arr[-2]
#2: arr[-2:]와 arr[-4:-2]
#3: arr[-3:]와 arr[-6:-3]

def check(arr):
    if arr[-1]==arr[-2] or arr[-2:]==arr[-4:-2] or arr[-3:]==arr[-6:-3]:
        return False
    return True
def dfs(box):
#    if len(box)==0 or 1 :
#        return 4
#    if 1 < len(box) < 6:
#        if len(box) == 2 or 3:
#            if box[-1] == box[-2]:
#                return 3
#        if len(box) == 4 or 5:
#            if box[-1] == box[-2] or box[-2:] == box[-4:-2]:
#                return 2
#    if not check(box):
#
#        return 1
    ####
    if len(box) == n:
        if check(box):
            return box
    for i in range(4,7):
        dfs(box+[i])

n = int(input())
if n == 1:
    print(4)
    exit(0)
elif n==2:
    print(45)
    exit(0)
elif n==3:
    print(454)
    exit(0)
print(dfs([]))