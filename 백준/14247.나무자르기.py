n = int(input())
tree = list(map(int,input().split()))
growth = list(map(int,input().split()))
arr = []
for i in range(n):
    arr.append((tree[i],growth[i]))
arr=sorted(arr,key=lambda x : x[1])
res=[]
for i in range(n):
    res.append(arr[i][0]+i*arr[i][1])
print(sum(res))



#자료형(사전)과 배열 의 성질차이
#자라는 길이순으로 배열을해서