쪽#오른개행제거
import sys
a,b=map(int,sys.stdin.readline().split())
dic_1={}
dic_2={}
for i in range(1,a+1):
    k=sys.stdin.readline().rstrip() #키:숫자, 값:포켓몬이름
    dic_1[str(i)]=k
    dic_2[k]=str(i) #키:포켓몬이름, 값:숫자

for j in range(b):
    x=sys.stdin.readline().rstrip()
    if x in dic_1 :
        print(dic_1[x])
    else :
        print(dic_2[x])