import sys
from collections import Counter
n=int(sys.stdin.readline())
arr=[]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
cnt_arr = Counter(arr).most_common()#최빈값-빈출?

print(round(sum(arr)/n)) #산술평균
print(arr[n//2]) #중간값
if len(cnt_arr) > 1 :
    if cnt_arr[0][1] == cnt_arr[1][1]: #구현해보기
        print(cnt_arr[1][0])
    else : print(cnt_arr[0][0])

else : print(cnt_arr[0][0])
print(arr[-1]-arr[0])


