n , m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

def get_num_of_gold(row, col, k):
    return sum([
        grid[i][j]
        for i in range(n)
        for j in range(n)
        if abs(row - i) + abs(col - j) <= k
    ])


def get_num_of_gold(row, col, k):
    return sum(
        [grid[i][j] for i in range(n) for j in range(n) if abs(row - i) + abs(col - j) <= k])