import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [i for i in range(n+1)]

def find_parent(x):
    if arr[x] == x:
        return x
    arr[x] = find_parent(arr[x])
    return arr[x]

def union(a,b):
    x = find_parent(a)
    y = find_parent(b)
    if x==y:
        return
    arr[x] = y
    return

for i in range(m):
    k, a, b = map(int,input().split())
    if k == 0:
        union(a,b)
    else:
        resa,resb = find_parent(a), find_parent(b)
        if resa == resb:
            print("YES")
        else:
            print("NO")


# print(arr)



#
# arr = []
# dic = dict()
# now = 1
# for i in range(m):
#     k, a, b = map(int, input().split())
#     if k == 1:
#         arr.append([a,b])
#         if a in dic and b in dic:
#             if dic[a] == dic[b]:
#                 print("YES")
#             else:
#                 print("NO")
#         else:
#             print("NO")
#     #k == 0, a,b가 합집합일때
#     else:
#         if a in dic and b in dic:
#             num = dic[b]
#             for j in dic:
#                 if dic[j] == num:
#                     dic[j] = dic[a]
#         elif a in dic:
#             dic[b] = dic[a]
#
#         elif b in dic:
#             dic[a] = dic[b]
#
#         else:
#             dic[a] = dic[b] = now
#             now += 1
#
#     # print(a,b,"dic :" , dic)
#
#
#
# # print(dic)
