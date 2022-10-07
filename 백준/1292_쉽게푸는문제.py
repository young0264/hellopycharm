import sys
input=sys.stdin.readline
a, b = map(int,input().split())
arr=[]
for i in range(1,50):
    for j in range(i):
        arr.append(str(i))  #숫자형태의 문자가 들어가있는 리스트 arr
res=[]
s=0
for i in arr:
    res.append(int(i))  #res 에 정수형 수열완성
for j in range(a-1,b):
    s+=res[j]
print(s)
#두자리의 입력에 대해서 주의. join사용 x