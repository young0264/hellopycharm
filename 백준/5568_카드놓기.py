from itertools import permutations
n = int(input())
k = int(input())
arr = []
for i in range(n):
    arr.append(str(input()))
#arr = set(arr)
new = list(permutations(arr,k))
res = []
for i in set(new):
    res.append(''.join(i))
print(len(set(res)))
