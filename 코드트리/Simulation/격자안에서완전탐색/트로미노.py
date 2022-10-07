n , m = map(int,input().split())
block = [ list(map(int,input().split())) for _ in range(n)]

shapes = [
    [[1, 1, 0],
    [1, 0, 0],
    [0, 0, 0]],

    [[1, 1, 0],
    [0, 1, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]],
]
def tetris(x,y):
    final_max = 0
    for i in range(6):
        #check = True
        shape_max = 0
        for dx in range(3):
            for dy in range(3):
                if shapes[i][dx][dy] == 0 :    #x,y 자리위치에 대해
                    continue
                if x+dx >= n or y+dy >= m :
                    break
                else : # 1
                    shape_max += block[x+dx][y+dy]  #
        #if check :
        final_max = max(final_max, shape_max)
    return final_max
res=0
for i in range(n):
    for j in range(m):
        res=max(res,tetris(i,j))
print(res)
#왼쪽위 꼭지점을 기준을 잡는다는 개념으로
# 한꼭지점에서 생길수있는 도형의 모형들을 shapes에 담고
# 그 (x,y)라는 한꼭지점에 대해 shaepes들을 돌며 Max값을 리턴해주는 함수를 만들고
# 입력 모든 x,y를 돌며 모든 모양에대한 합의 최댓값을 출력해준다.
