# 1.defaultdict
from collections import defaultdict
t = int(input())
for i in range(t):
    dic = defaultdict(list)
    n = int(input())
    nrr = sorted(list(map(int, input().split())))
    m = int(input())
    mrr = list(map(int, input().split()))  ##target
    for i in range(len(nrr)):
        dic[nrr[i]]=1
    for i in range(len(mrr)):
        if dic[mrr[i]]:
            print(1)
        else: print(0)##
#2.set
t = int(input())
for i in range(t):
    n = int(input())
    nrr = set(map(int, input().split()))
    m = int(input())
    mrr = list(map(int, input().split()))  ##target
    ans = []
    for i in mrr:
        ans.append(['0','1'][i in nrr])
    print('\n'.join(ans))
#3.이분탐색
t = int(input())
for i in range(t):
    n = int(input())
    nrr = sorted(list(map(int, input().split())))
    m = int(input())
    mrr = list(map(int, input().split()))  ##target
    ans = []
    for target in range(len(mrr)):
        flag = 0
        s, e = 0, len(nrr)-1
        while s <= e:
            mid = (s + e) // 2
            if nrr[mid] > mrr[target]:
                e = mid - 1
            elif nrr[mid] < mrr[target]:
                s = mid + 1
            else:
                print(1)
                flag = True
                break
        if flag:
            continue
        else:
            print(0)

