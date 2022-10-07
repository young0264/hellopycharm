a, b, n = map(str,input().split())
chess = [[0]*8 for _ in range(8)]
arr = []
king = [0,0]        #[]첫번째가 y좌표, []두번째가 x좌표
stone = [0,0]
for i in range(int(n)):
    arr.append(input())
king[1] = ord(a[0])-65
king[0] = int(a[1]) -1
stone[1] = ord(b[0])-65
stone[0] = int(b[1])-1

for move in arr:
    king_copy = king
    stone_copy = stone
    if move == 'R':
        king[1] += 1
        if king == stone:
            stone[1] +=1
    elif move == 'L':
        king[1] -= 1
        if king == stone:
            stone[1] -=1
    elif move == 'B':
        king[0] -= 1
        if king == stone:
            stone[0] -= 1
    elif move == 'T':
        king[0] += 1
        if king == stone:
            stone[0] += 1

    elif move == 'RT':
        king[0] +=1
        king[1] +=1
        if king == stone:
            stone[0] +=1
            stone[1] +=1

    elif move == 'LT':
        king[1] -=1
        king[0] +=1
        if king == stone:
            stone[1] -= 1
            stone[0] += 1

    elif move == 'RB':
        king[1] +=1
        king[0] -=1
        if king == stone:
            stone[1] +=1
            stone[0] -=1

    elif move == 'LB':
        king[0] -= 1
        king[1] -= 1
        if king == stone:
            stone[0] -=1
            stone[1] -=1
    if  0>king[0] or king[1]>=8 or 0>king[1] or king[0]>=8 :

        king[0] = king_copy[0]
        king[1] = king_copy[1]
        print(king, king_copy)

    #if  0>stone[0]>=8 or 0>stone[1]>=8:
    #    stone = stone_copy


