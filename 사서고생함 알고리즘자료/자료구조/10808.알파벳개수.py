# 97~122 소문자
arr=[]
arr_cnt=[0]*26
n=input()
for k in range(97,123,1):
    arr.append(k)

for i in n:
    for j in range(26):
        if ord(i) == arr[j]:
            arr_cnt[j] += 1
        else : arr_cnt[j] += 0

for i in arr_cnt:
    print(i)
