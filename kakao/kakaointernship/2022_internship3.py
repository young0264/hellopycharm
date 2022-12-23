# 경험치가 없을수도 있고. -> if rwd_1,2가 0이면 => 시간별로 증가시키기
# 현재의 알고력이나 코딩력이 다음점을 넘게되면 멈추고
def solution(alp, cop, problems):
    ans = 0  # 문제푸는데 걸리는 총 시간
    for i in range(len(problems)):
        # 첫번째 값이거나,능력치 증가가 0 이면 시간으로 능력치 상승##시간으로+
        if i == 0 or (problems[i][2] == 0 and problems[i][3] == 0):
            if alp - problems[i][0] < 0:
                ans += problems[i][0]-alp
            if cop - problems[i][1] < 0:
                ans += problems[i][1]-cop
            ans += problems[i][4]
            alp = problems[i][0] + problems[i][2]
            cop = problems[i][1] + problems[i][3]
            #print(alp,cop,ans)
        else:  # 문제를 풀면서 경험치 쌓기
            if alp < problems[i][0] and cop < problems[i][1]:#둘다 작아야대
                #print(alp,cop)
                if problems[i-1][2]==0:#alp경험치가 0
                    k = (problems[i][1] - cop) // problems[i-1][3]
                    #alp += problems[i][2] * k
                    cop += problems[i][3] * k
                    ans += k*problems[i-1][4]
                elif problems[i-1][3]==0:#cop경험치가 0
                    k = (problems[i][0] - alp) // problems[i-1][2]
                    alp += problems[i][2] * k
                    #cop += problems[i][3] * k
                    ans += k*problems[i-1][4]
                else:
                    k = min((problems[i][0] - alp) // problems[i-1][2], (problems[i][1] - cop) // problems[i-1][3])
                    alp += problems[i-1][2] * k
                    cop += problems[i-1][3] * k
                    ans += k*problems[i-1][4]
                    #print(k,alp,cop,ans)
                #print(alp,cop)
            elif alp == problems[i][0]:
                cop = problems[i][1]
                ans += problems[i][1]-cop
            elif cop == problems[i][1]:
                alp = problems[i][0]
                ans += problems[i][1]-alp


    return print(ans)
solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]	)