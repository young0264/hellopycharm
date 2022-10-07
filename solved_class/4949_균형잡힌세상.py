
#stack==0 인거하고 if not stack하고 같은가?
#(,[ 주어지면 배열에 쌓고 )or]이게 주어지면
#arr=[] while문밖에?
#flag=0
while True:
    n = input().rstrip() # split하고 출력이 아예달리나옴. 한글자씩다체크
    arr = []
    flag = 0
    if n==".":
        break
#소/대로나눠서
    for i in n:
        if i=="(" or i=="[":
            arr.append(i)
        elif i==")":
            if not arr or arr[-1]=="[":
                print("no")
                flag=1 # 이걸 왜 넣는걸까
                break #브레이크?
            else :
                arr.pop()
        elif i=="]":
            if not arr or arr[-1]=="(": #or arr:
                print("no")
                flag=1
                break
            else :
                arr.pop()

    if flag == 0 :#들여쓰기가 헷갈리네
        if not arr :
            print("yes")
        else :#열린것만 들어갔을때
            print("no")



