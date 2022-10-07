#연속된 k개 요소의 최대 합 구하기

def max_sum(arr,n,k):
    max_value = 0
    if n < k:
        return False
    window_sum = sum(arr[:k])
    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_value = max(max_value,window_sum)

    return max_value







# k종류의 알파벳으로 이루어진 가장 짧은 문자열 길이 찾기
def sliding_window(arr):
    n = len(arr)
    length = len(list(set(arr)))
    left, right = 0,0
    dic = dict()
    min_length = 0
    while right < n:
        if len(dic) < length:
            dic[arr[right]] = right
            right += 1

        if len(dic) == length:  #k종류
            mini = min(dic.values())
            for key,value in dic:
                if value == mini:
                    del dic[key]
                    left = mini + 1
                    break
        min_length = min(min_length,right-left)




