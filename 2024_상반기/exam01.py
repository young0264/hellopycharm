plants = [2, 3, 1, 2] # 며칠간 물을 안주면 죽는지 정보(2면 2일때 물 안주면 죽음)
watered = [3, 1, 2, 1, 4, 1] #물을 주는 plant의 idx 정보 -> [2, 0, 1, 0, 3, 0]
answer = [4, 2, 2, 2, 2, 1]

def solve1(plants, watered):
    n, m = len(plants), len(watered)
    # plantsLifeInfos = plants[::]
    plantsLifeInfos = [0]*n

    for i in range(m):
        watered[i] -= 1

    for i in range(m):
        waterPlantIdx = watered[i]
        # if plantsLifeInfos[waterPlantIdx] >= i+1 :
            plantsLifeInfos[waterPlantIdx] = plants[waterPlantIdx] + i

    print(plantsLifeInfos)





solve1(plants, watered)