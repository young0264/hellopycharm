#1.순열 2.재귀 3.dfs
N,K = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
res_num = 0
def f(check_zari,zz):       #여기에서 N은 들어오고. res_num은 글로벌해야하고.??
    global res_num
    #print(zz)
    if check_zari == len(str(N)): #마지막 자리까지 다 돌았고 zz

        if '0' not in str(zz):  #
            print(zz)
            res_num = max(res_num, zz)
        return  #if return문


    for i in range(K):
        num = arr[i]*(10**(len(str(N))-1-check_zari)) + zz
        if num <= N :
            f(check_zari+1,num) #다음자릿수, zz->num 큰자리수값 더하기
            #큰거부터 작은거가지 다 훑었는데 없다면
        else:
            f(check_zari +1,zz) #큰자리는 스킵하고 다음자리로
f(0,0)
print(res_num)























