n = 11
length = 1  # 자릿 수
endOfNum = 9  # 자릿수에 해당하는 숫자 수 #9,90,900,....
startOfNum = 1  # 자릿수에 해당하는 숫자 시작점 #1,10,100....
while (n > length * endOfNum):
    print(length * endOfNum)
    n -= length * endOfNum  # 덩어리치기

    endOfNum *= 10
    startOfNum *= 10
    length += 1
res = (n - 1) // length  # 뒤에 붙는 자릿수 나머지 숫자
idx = (n - 1) % length
expectLengthNum = (startOfNum + res)

answer = str(expectLengthNum)[idx]
print("answer:", answer)
