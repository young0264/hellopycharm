def solution(ingredients):
    answer = 0
    stack = [0]
    flag = 0
    for ingredient in ingredients:
        #     if stack[-4] == [1, 2, 3, 1]:
        #         answer+=1
        #         stack = stack[:-4] pop 4번
        if ingredient == 1:
            if flag and stack[-1] == 3:
                #                print("1", stack)
                stack.pop()
                stack.pop()
                stack.pop()
                answer += 1

            else:
                flag = 1
                stack.append(1)

        elif ingredient == 2:
            if flag and stack[-1] == 1:
                stack.append(2)
                flag = 1
            else:
                flag = 0
                stack.append(2)

        elif ingredient == 3:
            if flag and stack[-1] == 2:
                stack.append(3)
            else:
                flag = 0
                stack.append(3)
    # print("ing,flag",ingredient, flag,stack)

    return answer