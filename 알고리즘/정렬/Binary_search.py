def binary_search(arr,target,start,end):#인덱스 구하는 코드
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif target < arr[mid] :
            end = mid-1
        else : # target > arr[mid]
            start = mid+1
    return None


