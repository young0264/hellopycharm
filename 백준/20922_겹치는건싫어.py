n, k = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, 0
visited = [0] * (max(arr) + 1)
cnt = 0
answer = 0
# 해당값의 제일처음나온 인덱스를 짤라야하는거야.
for right in range(len(arr)):
    visited[arr[right]] += 1
    if visited[arr[right]] > k:

        answer = max(answer, right - (left + 1))
        # print(left,right)
        for i in range(left, right):
            if arr[i] == arr[right]:
                left = i + 1
                break
        visited[arr[right]] -= 1
answer = max(answer, right - left)
# print(visited)
print(answer + 1)
