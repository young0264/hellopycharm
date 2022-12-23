def solution(low, high, ximg):
    img = []
    for i in ximg:
        img.append(list(i))
    for i in img:
        print(i)
    answer = 0
    c = len(img[0])
    r = len(img)

    def check(x1, x2, y1, y2):
        black, white = 0, 0
        nr = len(img)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if img[i][j] == '#':
                    black += 1
                else:
                    white += 1
        if low <= (black / (nr * nr)) * 100 < high:
            return True
        else:
            return False

    for i in range(r):
        for j in range(c):
            flag = 0
            res = 0
            for k in range(i, r):
                for l in range(j, c):
                    # i~k , j~l
                    if not flag:
                        if img[i][l] != '#' or img[k][j] != '#' or img[k][l] != '#' or img[k][j] != '#':
                            flag = 1

                    if k - i == l - j:
                        if check(i, k + 1, j, l + 1):
                            res += 1
            if not flag and res == 1:
                answer += 1

    return answe