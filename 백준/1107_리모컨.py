import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
err = list(map(int,input().split()))    #고장난 리모컨 번호
remote =[]  #멀쩡한 리모콘 번호
cnt = abs(100-N)
if N == 100:
    print(0)
    exit(0)
for t in range(10):
    if t in err:
        continue
    remote.append(t)
for i in range(1000001):
    tmp = str(i)
    a=False
    for j in tmp:
        if int(j)  in err:
            a=True
            break
    if a:
        continue
    else:
        cnt = min(cnt , abs(N-i) + len(str(i)))
print(cnt)






#check_remote =''   #체킹용 리모콘번호   #545
#for j in N :
#    if int(j) in remote:
#        check_remote = check_remote +str(j)
#cha = len(N)-len(check_remote)
#
#for i in range(int(cha)):
#    for j in remote:
#        res.append(check_remote+str(j))
#
#for t in res:
#    answer.append(abs(int(N) - int(t)))
#
#print(check_remote)
#print(len(N)+min(answer))