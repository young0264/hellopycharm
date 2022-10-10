t = int(input())
arr = ['','+','-']
for _ in range(t):
    n = int(input())
    box = []


def dfs(num,cnt,value):#cnt 0부터
    if cnt == n:
        if value==0:
            print(''.join(box))
    box.append(num)
    for i in range(3):
