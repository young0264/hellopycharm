import sys
h = []
l = []
answer = sys.maxsize
for i in range(3):
    h.append(int(input()))
for i in range(2):
    l.append(int(input()))

for i in range(3):
    for j in range(2):
        answer = min(answer,h[i]+l[j])
print(answer-50)