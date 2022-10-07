t=int(input())
arr=[]
for _ in range(t):
    grade=list(input().split())
    arr.append(grade)
arr.sort(key=lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0])) #이곳에 -를 넣어서 역순으로 하고싶은데 안되네요 ㅠ
for i in arr:
    print(i[0])