from collections import deque
T = int(input())
for _ in range(T):
    left_arr = deque()
    right_arr = deque()
    s = input()
    for i in s:
        if i == '<':
            if left_arr:
                right_arr.appendleft(left_arr.pop())
        elif i == '>':
            if right_arr:
                left_arr.append(right_arr.popleft())
        elif i == '-':
            if left_arr:
                left_arr.pop()
        else:
            left_arr.append(i)
    print(''.join(left_arr)+''.join(right_arr))
