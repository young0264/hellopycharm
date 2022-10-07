t = int(input())
for i in range(t):
    box = []
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    len = n//2
    res = 0


   # while len(arr) > 1:
   #     if n%2 ==0:
   #         for j in range(len):
   #             box.append(arr[j]+arr[-j-1])
   #         arr = box
   #         res += sum(box)
   #         box = []
   #         print(res)
    print(arr)
    print(99+38+35+25+25+24+22+19)
       # elif n%2 != 0:
       #     for j in range(len):
       #         box.append(arr[j]+arr[-j-1])
       #     box.append(arr[len]+min(box))
       #     print(arr)
       #     print(sum(box)*2)
