def solution(order):
    answer = 0
    length = len(order)
    order_arr = [0] * length
    sub_arr = [0]

    for i in range(length):
        order_arr[order[i] - 1] = i + 1
    print(order_arr)

    pos = 1
    idx = 0

    while True:
        print("order_arr",order_arr)
        print("sub_arr",sub_arr)

        if length > idx and order_arr[idx] == pos:

            idx += 1
            pos += 1
            answer += 1
        elif sub_arr[-1] == pos:
            sub_arr.pop()
            pos += 1
            answer += 1
        else:
            if idx == length:
                break
            sub_arr.append(order_arr[idx])
            idx += 1

    print(answer)
    return answer
# solution([4, 3, 1, 2, 5])
solution([5, 4, 3, 2, 1])