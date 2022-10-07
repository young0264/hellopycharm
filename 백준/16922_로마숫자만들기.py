# 중복조합
from itertools import combinations_with_replacement as combi
n = int(input())
dic = {"I":1, "V":5, "X":10, "L":50 }
arr = ["I", "V", "X", "L"]
answer = 0
num_arr = []
answer_arr = []
length = len(arr)#4
#for res in(list(combi(arr,n))):
#    number = 0
#    for i in res:
#        number += dic[i]
#    num_arr.append(number)
#print(len(list(set(num_arr))))

def dfs(start,box):
    if len(box) == n:
        num_arr.append(box)
        return
    for i in range(start,length):
        dfs(i,box+[arr[i]])
dfs(0,[])
for ar in num_arr:
    number = 0
    for i in ar:
        number+=dic[i]
    answer_arr.append(number)
print(len(list(set(answer_arr))))



