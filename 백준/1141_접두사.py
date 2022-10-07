n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
#print(arr)
arr = set(arr)
arr = list(arr)
n = len(arr)

for i in range(n):
    flag = 0
    for j in range(n):
        if arr[i][0] == arr[j][0]:
            for t in range(1,len(arr[j])+1):#문자서칭
                if arr[i] == arr[j][:t]:
                    flag += 1
            if flag >=2:
                n -= 1

print(n)