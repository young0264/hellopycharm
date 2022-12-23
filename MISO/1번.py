# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(inner, outer, points_x, points_y):
    # write your code in Python 3.8.10

    answer = 0
    length = len(points_x)

    for i in range(length):
        dist = points_x[i]**2 + points_y[i]**2
        if inner**2 < dist < outer**2:
            answer += 1
    return answer

    pass
