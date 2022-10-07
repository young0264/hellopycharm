#파라메트릭서치란 최적화 문제를 결정문제 (예 혹은 아니오)로 바꾸어 해결하는 기법
    # 예시 : 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
#일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있다.
#이진탐색->높이h
#이 높이로 잘랏을때 조건만족 가능? yes or no
#높이가 0~10억 -> 이진탐색 // 잘린떡의 길이의 합
#------------------------------------------------------------

n,m = list(map(int, input().split(' '))) #떡의 개수(n)과 요청한떡길이 m
array = list(map(int,input().split())) #각 떡의 개별 높이 정보입력

#이진 탐색을 위한 시작점과 끝점 설정
result=0
start=0
end=max(array)

while(start<=end):
    total=0
    mid = (start + end)//2
    for x in array:         #잘랐을 때의 떡의 양 계산
        if x > mid :
            total += x - mid

    if total < m :  #왼쪽부분탐색
        end = mid -1
    else :
        result = mid  #잘?#떡양이 부족 -> 덜자르기 #오른쪽부분탐색 . 여기에 result에기록
        start = mid +1
#높이의최댓값출력
print(result)