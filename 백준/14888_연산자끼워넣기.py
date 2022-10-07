from itertools import permutations
import sys
input = sys.stdin.readline
#'/' 하고 '//' 각각 1개가 아니야?
n = int(input())
num = list(map(int,input().split()))    #숫자리스트
l = list(map(int,input().split()))  #연산자리스트
l_1 = ['+','-','*','/']
arr = []
for i in range(4):
    arr.extend(l[i]*l_1[i])
arr = list(set(permutations(arr,n-1)))
max_num = -sys.maxsize
min_num = sys.maxsize
num_list = []
for i in arr:
    res = num[0]
    for j in range(n-1):    #0부터
        if i[j]=='+':
            res = res + num[j+1]
        elif i[j]=='-':
            res = res - num[j + 1]
        elif i[j]=='*':
            res = res * num[j + 1]
        else:
            if res < 0:
                res=res*-1
                res = res // num[j + 1]
                res=res*-1
            else:
                res = res // num[j+1]
    max_num = max(max_num,res)
    min_num = min(min_num,res)
print(max_num)
print(min_num)