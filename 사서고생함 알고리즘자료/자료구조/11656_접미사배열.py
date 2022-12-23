a=list(input())
arr=[]
for i in range(len(a)):
    arr.append(a[i:len(a):1])

arr.sort()
for i in range(len(a)):
    print(''.join(arr[i]))

#왼쪽 원소들을 하나씩 제거하면서 [0] [1] [2] arr에 추가해주기
#or i부터 len(a)까지 입력받기
