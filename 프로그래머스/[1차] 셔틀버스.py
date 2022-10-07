def solution(n, t, m, timetable):
    answer = ''
    bustimes = []
    people_time = []
    for time in timetable:
        a,b = map(int,time.split(":"))
        res = a*60 + b
        print(res)
        people_time.append(res)
    for i in range(n):
        bustimes.append(540 + i*t)
    people_time.sort()
    print("bustimes",bustimes)
    print("people_time",people_time)
    idx = 0
    flag = 0
    for bustime in bustimes:
        cnt = 0
        for i in range(idx,len(timetable)):
            idx = i+1
            if people_time[i] < bustime:
                print("123",people_time[i])
                cnt += 1
            elif cnt == m and not flag:
                print(123123)
                flag = 1
                answer = people_time[i] - 1
            else:
                break
        print()

    print('ans',answer)


    return answer

n,t,m,timetable = 2,10,2,["09:10", "09:09", "08:00"]
solution(n, t, m, timetable)