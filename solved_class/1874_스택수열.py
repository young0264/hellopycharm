n=int(input())
arr=[]
arr_2=[]
#arr_3=[]    #+-
cnt=0
x=True
for i in range(n):
    a=int(input()) #4,3,6,8,7,5,2,1
    while a > cnt:  #"<= 와 ==" 차이 *범위설정 잘 해야함.!
        cnt += 1
        arr.append(cnt)
        arr_2.append('+')

    if arr[-1] == a:
        arr.pop()
        arr_2.append('-')
    else :
        x=False
        break
if x==True:
    for i in arr_2:
        print(i)
elif x==False:
    print("NO")
