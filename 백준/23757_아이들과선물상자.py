import heapq

#내림차순으로 가장 큰것을 heap 에서 pop할시엔 마이너스로 저장되고, 마이너스로 저장해야함을 주의

n, m = map(int, input().split())
a = list(map(int, input().split()))
brr = list(map(int, input().split()))

arr = []
for i in a:
    heapq.heappush(arr, -i)


for i in brr:
    wish = i
    present = -heapq.heappop(arr)
    if present >= wish:
        heapq.heappush(arr,-(present-wish))
    elif present < wish:
        print(0)
        exit(0)


print(1)


