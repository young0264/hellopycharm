#구현을 어케하지
#from itertools import permutations
import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int,input().split()))
sn = list(map(int,input().split()))
max_value = -sys.maxsize
min_value = sys.maxsize
res=[]
def dfs(index,now,add,sub,mul,div):
    global max_value, min_value
    if index >= n:
        max_value = max(max_value,now)
        min_value = min(min_value,now)
        return
    if add > 0:
        dfs(index+1,now + num[index],add-1,sub,mul,div)
    if sub > 0:
        dfs(index+1, now-num[index], add, sub-1, mul, div)
    if mul > 0:
        dfs(index+1, now*num[index], add, sub, mul-1, div)
    if div > 0:
        dfs(index + 1, now//num[index] if now > 0 else -((-now) // num[index]), add, sub, mul, div - 1)
        #if now > 0:
        #    dfs(index+1, now//num[index], add, sub, mul, div-1)
        #else:
        #    dfs(index+1, -((-now)//num[index]), add, sub, mul, div-1)

dfs(1,num[0],sn[0],sn[1],sn[2],sn[3])
print(max_value,min_value,sep='\n')

