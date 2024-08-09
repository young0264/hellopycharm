
def solution(histogram):
    answer = 1
    len_y = len(histogram)
    len_x = len(histogram[0])

    # y축의 높은 순서부터 search
    for j in range(len_x):
        cnt = 1
        for i in range(len_y):
            #중간에 그래프의 빈 좌표가 나올경우 cnt 초기화
            # 1이 먼저 나오면 그래프 높이는 확정
            # 2가 나오면 cnt 증가
            if histogram[i][j] == 0:
                cnt = 1
            elif histogram[i][j] == 1:
                break
            elif histogram[i][j] == 2:
                cnt += 1
        answer *= cnt

    return answer