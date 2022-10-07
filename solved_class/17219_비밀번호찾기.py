#컴마 단위로 분리되있는거 ㄷㄱ입력받기
import sys
m,n = map(int,input().split())
dic={}
arr=[]
for i in range(m):
    a,b=sys.stdin.readline().split()
    dic[a]=b
for j in range(n):
    print(dic[input()])

