m1, d1, m2, d2 = map(int,input().split())
dow = input()
day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
answer = 0


def find_total_day(month, day):
    res = 0
    for i in range(1, 13):
        if i == month:
            res += day
            return res
        else:
            res += days[i]
    return res


start_total_day = find_total_day(m1, d1)
end_total_day = find_total_day(m2, d2)

answer += (end_total_day-start_total_day)//7
idx = (end_total_day-start_total_day)%7

for i in range(1,idx+1):
    if day_of_week[i] == dow:
        answer += 1
print(answer)





