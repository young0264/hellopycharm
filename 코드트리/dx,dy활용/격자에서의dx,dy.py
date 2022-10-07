#1. 앞에가 행, 뒤에가 열 ##행열로 읽으면 편해.
#2. zip함수 사용
#zip 함수는 넘긴 인자에 list나 tuple같이 순회가 가능한 변수를 여러 개 넘기면,
# 순서대로 첫 번째 원소부터 끝 원소까지 쌍으로 값을 뽑아주는 함수입니다.
# in_range와 같이 범위를 확인하는 조건의 경우에는
# 항상 if문 가장 앞에 작성하는 것이 정말 중요합니다.
#i/j   0 1 2 3 4        이미지 좋네 ㅎ
#  ---------------
#0|    0 0 0 1 0
#1|    0 1 1 1 0
#2|    0 0 0 0 1
#3|    1 0 1 1 1
#4|    1 0 1 1 0

dx = [0,-1,0,1]
dy = [1,0,-1,0]

def in_range(x, y):
    return 0 <= x and x < 5 and 0 <= y and y < 5











arr1=[1,2,3,4]
arr2=[11,22,33,44]
for a,b in zip(arr1,arr2):
    print(a,b)
print(list(zip(arr1,arr2)))

def in_range(x, y): #표현식. True를 반환오....
    return 0 <= x and x < 5 and 0 <= y and y < 5

print(in_range(1,1))