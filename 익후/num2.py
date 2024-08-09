n = 111 # n번째

length = 1 # 자릿 수
endOfNum = 9 # 자릿수에 해당하는 숫자 수 #9,90,900,....
totalLength = endOfNum*length

startOfNum = 1 # 자릿수에 해당하는 숫자 시작점 #1,10,100....


while(n > length * endOfNum):
# while(n > totalLength):
    print(length * endOfNum)
    # print(totalLength)
    n -= length * endOfNum # 덩어리치기
    # n -= totalLength
    endOfNum *= 10
    startOfNum *= 10
    length += 1

# 10~99
# 100~999
print("n:",n)

# startOfNum += (n - 1) // length
# s = str(startOfNum)

res = startOfNum + n
print("res:",res)
# print("s:",s)
# print("res:",int(s[(n - 1) % length]))

# print(totalLength)
# print(length * endOfNum)
# print(startOfNum)




