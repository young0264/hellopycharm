def solution(levels):
    answer = 0

    def top_25_percent(arr):
        sorted_arr = sorted(arr, reverse=True)
        twenty_five_percent = int(len(arr) * 0.25)
        top_25_percent_elements = sorted_arr[:twenty_five_percent]
        return top_25_percent_elements

    if (len(levels) < 4):
        return -1
    answer = top_25_percent(levels)[-1]

    return answer