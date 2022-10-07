n=int(input())
dic={}
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort()
for i in arr :
    if i in dic :
        dic[i] += 1
    else : dic[i]=1

max_key = max(dic, key=dic.get)
        #만약 많이 가지고 있는 정수가 여러가지라면. 작은것을 출력한다.
print(max_key)
print((dic))