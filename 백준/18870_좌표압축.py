import sys
input = sys.stdin.readline
n=int(input())
dic={}
arr = list(map(int,input().split()))
new_arr = set(arr)
real_arr=[]
for i in new_arr:
    real_arr.append(i)
real_arr.sort()
for i in range(len(real_arr)):
    dic[real_arr[i]] = i

for i in arr:
    print(dic[i])