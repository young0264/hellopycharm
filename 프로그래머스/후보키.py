from itertools import combinations


def solution(relations):
    answer = 0
    number_arr = [i for i in range(len(relations[0]))]
    ans_arr = []
    for i in range(1,len(relations[0])+1):
        for num in combinations(number_arr,i):
            # print("num",num)#0,1,2,3, 01 02 03 .....
            arr = []
            for relation in relations:
                res = ''
                for n in num:
                    res += relation[n]
                arr.append(res)
            # print("arr",arr)
            a = (len(arr))
            b = (len(list(set(arr))))
            # print("length,num",a,b,num)
            if a==b:
                ans_arr.append(num)
    # print("ans_arr",ans_arr)
    now = [-1]
    for ans in ans_arr:
        # print("now",now)
        flag = 0
        for i in now:
            if i in ans:
                flag = 1
                # print(123123123,"ans",ans)
                break
            else:
                print("i :",i )
                print(12312313,"now",now)
                print("ans",ans)
        if not flag:
            now = ans
            answer+=1
        print()
    print(answer)
    return answer
solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])