def solution(noti_time, do_not_disturb):
    answer = "impossible"
    do_not_disturb_minute = []
    time_visited = [0] * 1440

    # 시:분 문자열 -> 분으로 치환 return
    def strTimeToMinutes(strTime):
        h_time, m_time = strTime.split(":")
        minutes = int(h_time) * 60 + int(m_time)
        return minutes

    def minutesToStrTime(minutes):
        if minutes == 0:
            return "00:00"

        h = minutes // 60
        m = 0

        if h >= 1:
            m = minutes % h
        else:
            m = minutes

        strTime = str("{:02d}".format(h)) + ":" + str("{:02d}".format(m))
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

    if time_visited[strTimeToMinutes(noti_time)] == 0:
        return noti_time
    else:
        flag = 0
        for i in range(strTimeToMinutes(noti_time), 1440):
            if time_visited[i] == 0:
                return minutesToStrTime(i)
        if flag == 0:
            for i in range(0, 1440):
                if time_visited[i] == 0:
                    return minutesToStrTime(i)

    return answer

a = "a,b,c"
a.split(",")