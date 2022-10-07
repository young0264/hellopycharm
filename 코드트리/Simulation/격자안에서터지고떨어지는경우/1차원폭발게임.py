#연속되는걸 반복해서 없애주는거네
n, m = map(int,input().split())
arr = [int(input()) for i in range(n)]

def correct(x,nx):
    return arr[x] == arr[nx]

#시작위치를 기준으로 끝위치를 반환하는 함수,
def end_point(start_idx,current_num):
    for i in range(start_idx+1,len(arr)):
        if arr[i] != current_num:
            return i-1
    return len(arr)-1
#enumerate 사용
while True:
    did_explode = False #flag
    for current_idx , number in enumerate(arr):
        if number == 0 :
            continue
        end_idx = end_point(current_idx,number)
        if end_idx - current_idx+1 >= m:  #우와 표현. 대박. !
            arr[current_idx:end_idx + 1] = [0]*(end_idx +1 - current_idx)
            did_explode = True
    #print(arr)
    arr = list(filter(lambda x : x>0, arr))
    #arr을 0으로 초기화하고 줄여버려
    if not did_explode:
        break
print(len(arr))
for i in arr:
    print(i)
#def find_index():#시작과 끝위치를 찾는 함수->시작을 돌면서 그 시작에대한 끝을 찾는함수로
#    global arr
#    for i in range(0,n-1):
#        if correct(i,i+1):
#            index = min(index,i)
#            res.append(i)
#        else:
#            index2 = max(index2,i)
#            not_res.append(i)
#            if index != 100:
#                break
#    arr = arr[0:index] + arr[index2:]
#
#find_index()
#print(arr)
#print(index,index2)
#
#
#
