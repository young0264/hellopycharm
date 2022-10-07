from bisect import bisect_left
n = int(input())
dic=dict()
arr=[0]*101
HP = list(map(int,input().split()))
happy = list(map(int,input().split()))
hp_arr = [0]*n
for i in range(1,n):
    hp_arr[i] = 100-HP[i]-HP[i-1]
hp_sumarr=[0]*n
print("hp_arr",hp_arr)
happy_arr=[0]*n #
for i in range(n):
    arr[HP[i]] = happy[i]
    dic[HP[i]] = happy[i]
print(dic)
new_dic = sorted(dic.items())
print(new_dic)
print("hp_arr",hp_arr)
for i in range(1,n):
    idx = bisect_left(hp_arr,100-hp_arr[i])
    if idx>0 and idx<n:
        hp_arr[idx] = hp_arr[idx-1]+hp_arr[i]
    print(hp_arr[i])
    print("idx",idx)
print(hp_arr)



