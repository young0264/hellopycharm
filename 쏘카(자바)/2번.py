# n=4, k=3, grid = [[1,2,2,2],[1,2,1,1],[1,2,2,1],[3,2,1,1]]
# 1 2 2 2 , 1 2 1 1, 1 2 2 1, 3 2 1 1

# n=3, k=2, grid = [[1,1,1],[1,2,2],[1,2,4]]
#

n = int(input())
k = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

for i in grid:
    print(i)


