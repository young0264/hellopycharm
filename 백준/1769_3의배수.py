s = input()
res = 0
cnt = 0
if len(s)==1:
    if int(s)%3 ==0:
        print(0, "YES", sep='\n')
    else:
        print(0, "NO", sep='\n')
    exit(0)

while True:
    cnt += 1
    for i in s:
        res += int(i)

    if res//10 == 0:
        break
    else:
        s= str(res)
        res = 0
if res%3 ==0:
    print(cnt,"YES",sep='\n')
else:
    print(cnt,"NO",sep='\n')        print(0, "YES", sep='\n')



