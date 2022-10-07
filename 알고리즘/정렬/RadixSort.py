from collections import deque
def radix_sort(num_arr):
    buckets = [deque() for _ in range(10)]
    max_value = max(num_arr)
    current_t = 1
    que = deque()
    que.extend(num_arr) # or que = deque(num_arr)

    while max_value >= current_t:
        while que:
            num = que.popleft()
            buckets[(num//current_t)%10].append(num)

        for bucket in buckets:
            while bucket:
                que.append(bucket.popleft())

        current_t *= 10
    return list(que)
arr = 	[3, 30, 34, 5, 9]
print(radix_sort(arr))
