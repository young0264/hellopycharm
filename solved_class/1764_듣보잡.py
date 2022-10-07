#a,b를입력받고 a,b에 해당하는 수만큼입력을 각 각 배열에 저장.
#두 배열을 셋집합으로 교집합만 골라내서 갯수와 값 순차출력
import sys
a,b = map(int,sys.stdin.readline().rstrip().split())
arr_a=[]
arr_b=[]
for _ in range(a):
    i=sys.stdin.readline().rstrip()
    arr_a.append(i)

for _ in range(b):
    j=sys.stdin.readline().rstrip()
    arr_b.append(j)

arr_s = list(set(arr_a) & set(arr_b))
arr_s.sort()
print(len(arr_s))
for k in arr_s:
    print(k)
