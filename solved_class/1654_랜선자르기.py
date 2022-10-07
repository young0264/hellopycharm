a,b=map(int, input().split())
start=1 #1
arr=[int(input()) for _ in range(a)] #arr배열에 랜선길이 입력
#end=(max(arr)) #무지성큰수
end = sum(arr)//b      #유지성큰수

while start <= end:
    mid = (start + end) // 2
    lanline = 0 #랜선수
    #arr_m = [(i // mid) for i in arr]#이 몫 리스트의 합이 b값이지
    for i in arr :
        lanline += i // mid

    if lanline >= b :
        start = mid +1 #왜 ㅠㅠ
    else :
        end = mid -1 #왜 ㅠㅠ

print(end)



#mid로 나눈 각 랜선길이의 몫의 합이 11이 되는 수 중 최대
