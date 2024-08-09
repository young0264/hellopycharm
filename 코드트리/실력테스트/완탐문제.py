import sys
#arr1, arr2에서 하나씩 뺀후의 차이가 최소로
n = int(input())
seq1 = list(map(int,input().split()))
seq2 = list(map(int,input().split()))
answer = sys.maxsize
#최대-최소 vs 최소-최대
sum1 , sum2 = sum(seq1), sum(seq2)
arr1 = []
arr2 = []
for i in range(n):
    arr1.append(sum1-seq1[i])
    arr2.append(sum2-seq2[i])
print(arr1)
print(arr2)
for i in range(n):
    for j in range(n):
        answer = min(answer, abs(arr1[i]-arr2[j]))
        print(answer)
print(answer)
# 4
# 10 13 17 3
# 21 22 11 13