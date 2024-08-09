def solution(noti_time, do_not_disturb):
    answer = "impossible"
    do_not_disturb_minute = []
    time_visited = [0] * 1440

    def int_to_padding_str(num):
        return "{:02d}".format(num)

    # 시:분 문자열 -> 분으로 return
    def strTimeToMinutes(strTime):
        h_time, m_time = strTime.split(":")
        minutes = int(h_time) * 60 + int(m_time)
        return minutes

    # int형 분 -> 시:분 문자열로 return
    def minutesToStrTime(minutes):
        strTime = "00:00"
        if minutes == 0:
            return strTime

        h = minutes // 60
        m = 0

        if h >= 1:
            m = minutes % (h*60)
        else:
            m = minutes
        print("minutes",minutes)
        print("h" ,h )
        print("m" ,m )

        strTime = int_to_padding_str(h) + ":" + int_to_padding_str(m)

        return strTime

    # ~ 기준으로 split -> 시작과 끝시간을 분으로 치환
    for time in do_not_disturb:
        start_time, end_time = time.split("~")
        do_not_disturb_minute.append([strTimeToMinutes(start_time), strTimeToMinutes(end_time)])

    # 분단위로 방문한 시간 check
    for start_min, end_min in do_not_disturb_minute:
        if start_min > end_min:
            for i in range(start_min, 1440):
                time_visited[i] = 1
            for i in range(0, end_min):
                time_visited[i] = 1
        else:
            for i in range(start_min, end_min):
                time_visited[i] = 1
    print(time_visited[60])
    print(strTimeToMinutes(noti_time))

    # if :ignore에 속하지 않는 시간대, else: 24시를 넘어가는지 확인
    if time_visited[strTimeToMinutes(noti_time)] == 0:
        return noti_time
    else:
        # noti_time부터 24시까지 check
        for i in range(strTimeToMinutes(noti_time), 1440):
            if time_visited[i] == 0:
                return minutesToStrTime(i)
        # 24시까지 방문이 되어있으면 0부터 끝까지 방문안한 첫지점 check
        for i in range(0, strTimeToMinutes(noti_time)):
            if time_visited[i] == 0:
                return minutesToStrTime(i)

    return answer
res = solution("01:11", ["01:11~01:12", "02:22~03:33"])
print(res)
print(23*60+59)