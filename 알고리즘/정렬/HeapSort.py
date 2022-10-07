#오름차순/
n = int(input())
arr = [0]+list(map(int,input().split()))

def heapify(arr,i,n):
    largest,left, right = i,i*2, i*2+1

    if left <= n and arr[largest] < arr[left]:
        largest = left

    if right <= n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        tmp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = tmp
        heapify(arr,largest,n)


def heap_sort(arr,n):
    #maxheap 만들어주고
    for i in range(n//2,0,-1):
        heapify(arr,i,n)

    for i in range(n,1,-1):
        tmp = arr[i]   #swap
        arr[i] = arr[1]
        arr[1] = tmp
        heapify(arr,1,i-1)

heap_sort(arr,n)
print(*arr[1:])
