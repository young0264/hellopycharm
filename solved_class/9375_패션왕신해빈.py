t = int(input())
for i in range(t):
    n=int(input())
    cloth_type = {}

    for j in range(n):
        cloth = list(input().split())
        #[0]:옷이름, [1]:옷타입
        if cloth[1] in cloth_type:
            cloth_type[cloth[1]].append(cloth[0])
        else :
            cloth_type[cloth[1]]=[cloth[0]]
    cnt=1
    for k in cloth_type: #키값빼내기
        cnt*=(len(cloth_type[k])+1)#키값k ->value+1
    print(cnt-1)


    #cloth_type을 cloth_type에 넣으면
    #dic[key]=value