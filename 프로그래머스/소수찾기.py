import math
from itertools import permutations
def solution(numbers):

    def prime_number(x):
        if x==2:
            return True
        elif x==1 or x==0:
            return False
        for i in range(2,int(math.sqrt(x))+1):
            if x%i == 0:
                return False
        return True

    num_arr = list(numbers)
    permu_arr = []
    answer = 0
    ansarr=[]
    for i in range(1,len(num_arr)+1):
        permu_arr.extend(list(permutations(num_arr,i)))
    for i in range(len(permu_arr)):
        x = ''.join(permu_arr[i])
        ansarr.append(int(x))
        ansarr = list(set(ansarr))
    for j in ansarr:
        if prime_number(j):
            answer+=1



solution("17")






#def solution(numbers):
#    answer = 0
#    x = 100
#    zero_cnt = 0
#    numbers_arr = []
#    for i in numbers:
#        if i == "0":
#            zero_cnt += 1
#        else:
#            numbers_arr.append(i)
#    numbers_arr.sort(reverse=True)
#    new_num = ''
#    for i in numbers_arr:
#        new_num += str(i)
#
#    x = int(new_num) * 10 ** (zero_cnt)
#    arr = [i for i in range(x + 1)]
#    res = []
#    for i in range(2, int(math.sqrt(x)) + 1):
#        if not arr[i]:
#            continue
#
#        for j in range(i * i, x + 1, i):
#            arr[j] = False
#    print("arr : ", arr)
#    for i in arr:
#        if i == 1:
#            continue
#        if i:
#            flag = 1
#            for num in str(i):
#                if num not in numbers:
#                    flag = False
#
#            if flag:
#                answer += 1
#                res.append(i)
#
#    print("========res=======")
#    print(res)
#    return answer
#solution("17")