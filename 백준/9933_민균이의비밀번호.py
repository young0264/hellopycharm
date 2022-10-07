n = int(input())
arr = []

for _ in range(n):
    pw = input()
    arr.append(pw)
for i in arr:
    ex = i[::-1]
    if ex in arr:
        #print(i[::-1])
        print(len(i),i[len(i)//2])
        exit(0)
