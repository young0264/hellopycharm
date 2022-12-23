def solution(s, times):
    answer = []
    day_arr = [0] * 32

    year, month, day, hour, minute, second = list(map(int, s.split(':')))
    total_sec = hour * 3600 + minute * 60 + second  # 기준점 시분초 -> 초 로 변환
    start_day = day
    end_day = 0

    day_arr[day] = 1

    for time in times:
        ntimes = list(map(int, time.split(':')))  # 일, 시간, 분, 초
        day += ntimes[0]  # 날짜는 바로 +1 해주기
        total_sec += ntimes[1] * 3600 + ntimes[2] * 60 + ntimes[3]
        new_day = (total_sec // 3600) // 24
        new_hour = (total_sec // 3600)
        new_min = (total_sec % 3600) // 60
        new_sec = (total_sec % 3600) % 60

        day += new_day
        hour += new_hour
        minute += new_min
        second += new_sec

        day_arr[day] = 1
        ## year에 반영하기

    for i in range(31, -1, -1):
        if day_arr[i] == 1:
            end_day = i
            break

    for i in range(start_day, end_day + 1):
        if day_arr[i] == 0:
            answer.append(0)
            break
    if not answer:
        answer.append(1)
    answer.append(end_day + 1 - start_day)

    return answer