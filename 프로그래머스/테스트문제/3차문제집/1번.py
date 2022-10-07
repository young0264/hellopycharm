import sys


def solution(a, b, n):
    answer = 0

    new_cola = n
    no_cola = 0
    least = sys.maxsize

    while new_cola > 0:
        new_cola = n // a
        least = n % a
        answer += new_cola * b
        n = new_cola * b + least
        print(answer)

    return answer