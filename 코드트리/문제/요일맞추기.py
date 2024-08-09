m1, d1, m2, d2 = map(int, input().split())
day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total_day = 0


def find_total_day(month, day):
    res = 0
    for i in range(1, 13):
        if i == month:
            res += day
            return res
        else:
            res += days[i]
    return res


res1 = find_total_day(m1, d1)
res2 = find_total_day(m2, d2)

# print(res1)
# print(res2)
if res1 > res2:
    res = (res1 - res2) % 7
    print(day_of_week[-res])
else:
    res = (res2 - res1) % 7
    print(day_of_week[res])
