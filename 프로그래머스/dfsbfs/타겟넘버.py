def solution(numbers, target):
    global answer
    answer = 0

    def dfs(value, idx):  # value = numbers[0], idx = 0
        global answer
        if idx == len(numbers):
            if value == target:
                #nonlocal answer
                answer += 1
            return

        dfs(value + numbers[idx], idx + 1)
        dfs(value - numbers[idx], idx + 1)

    dfs(0, 0)

    print(answer)


numbers = [1, 1, 1, 1, 1]
target = 3
solution(numbers, target)
