from bisect import bisect_left, bisect_right
def solution(words, queries):
    answer = []
    arr = [[] for _ in range(10001)]
    reversed_arr = [[] for _ in range(10001)]
    for word in words:
        arr[len(word)].append(word)
        # word = ''.join(list(reversed(word)))
        # print("word",reversed(word))
        reversed_arr[len(word)].append(word[::-1])
    #각 길이 위치 정렬
    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()
    for query in queries:

        if query[0]=='?':
            a = (query.replace('?', 'a'))
            b = (query.replace('?', 'z'))
            print("a,b",a,b)
            res1 = bisect_left(reversed_arr[len(query)], a[::-1])
            res2 = bisect_right(reversed_arr[len(query)], b[::-1])
            print("reversed_arr",reversed_arr)
            answer.append(res2-res1)
        else:
            a = query.replace('?', 'a')
            b = query.replace('?', 'z')
            res1 = bisect_left(arr[len(query)], a)
            res2 = bisect_right(arr[len(query)], b)

            answer.append(res2-res1)
    print("ans",answer)

    return answer

words , queries = ["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]
solution(words,queries)