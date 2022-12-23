import sys
def check_bw(matrix):
    case1 = 0
    case2 = 0

    for x in range(8):
        for y in range(8):
            if ((x % 2 == 0) and (y % 2 == 0)) or ((x % 2 == 1) and ( y % 2 == 1)):
                if matrix[x][y] != "B":
                    case1 += 1

            elif ((x % 2 == 0) and (y % 2 == 1)) or ((x % 2 == 1) and (y % 2 == 0)):
                if matrix[x][y] != "W":
                    case1 += 1

    for x in range(8):
        for y in range(8):
            if ((x % 2 == 0) and (y % 2 == 0)) or ((x % 2 == 1) and ( y % 2 == 1)):
                if matrix[x][y] != "W":
                    case2 += 1
            elif ((x % 2 == 0) and (y % 2 == 1)) or ((x % 2 == 1) and (y % 2 == 0)):
                if matrix[x][y] != "B":
                    case2 += 1
    return min(case1,case2)

def result():
    input_list=[]
    M,N = map(int, input().split())
    for idx in range(M):
        input_list.append([i for i in input().split()][:-1])


    min_revise_cnt=1234567898713434
    for row in range(M-7):
        for col in range(N-7):
            slice_mat = [one_row[col:col+8] for one_row in input_list[row:row+8]]
            revise_cnt=check_bw(slice_mat)
            min_revise_cnt = min(min_revise_cnt, revise_cnt)

    return min_revise_cnt
print(result())
