import sys
N,X = map(int,input().split())
visitors = list(map(int,input().split()))
#0부터시작
start = 0
curr_sum = 0
ans_arr = []
for idx,val in enumerate(visitors):
    max_value = -sys.maxsize
    curr_sum += val
    if idx - start +1 == X:
        max_value = max(max_value,curr_sum)
        ans_arr.append(max_value)
        curr_sum -= visitors[start]
        start += 1
ans = max(ans_arr)
ans_cnt = ans_arr.count(ans)
if ans == 0:
    print("SAD")
    exit(0)
print(ans)
print(ans_cnt)