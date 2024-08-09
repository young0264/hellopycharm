# numbers =[6,1,6,6,7,6,6,7]
numbers =[6,1,6,6,7,5,6,7]

defaultLength = len(numbers)

numDic = {}
maxLength = 0

for n in numbers:
    numDic[n] = numDic.get(n,0)+1
for i in numDic:
    if numDic[i] > defaultLength/2:
        print(i)
        exit(1)
print(-1)





