from itertools import product


# def find()

# def change_price(percent_combi):
#     global answer,imo_len,emoticons,users
#     new_emoticon_price = []
#     for i in range(imo_len):
#         res = emoticons[i]*(100-percent_combi[i])//100
#         new_emoticon_price.append(res)
#     return new_emoticon_price

def change_price0(price, percentage):
    res = price * (100 - percentage) // 100
    return res


def solution(users12, emoticons12):
    global answer, imo_len, emoticons, users
    users, emoticons = users12, emoticons12
    answer = []
    imo_len = len(emoticons)
    user_len = len(users)
    percent_arr = [10, 20, 30, 40]

    for percent_combi in product(percent_arr, repeat=imo_len):
        money = 0
        signup_user = 0
        for user in users:  # 각 유저마다
            user_percent, user_price, sum_cnt, sum_price = user[0], user[1], 0, 0

            for i in range(imo_len):
                if user_percent > percent_combi[i]:
                    continue
                else:
                    sum_cnt += 1
                    sum_price += change_price0(emoticons[i], percent_combi[i])

            if sum_price >= user_price:
                signup_user += 1
            else:
                money += sum_price

        answer.append((signup_user, money))

    answer.sort(key=lambda x: (x[0], x[1]))
    return list(answer[-1])