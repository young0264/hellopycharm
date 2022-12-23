from bisect import bisect_left
def solution(n, plans, clients):
    answer = []
    #mid = 0
    for client in clients:
        mid = 0
        left,right = 0,len(plans)-1
        while right>left:
            mid = (left+right)//2
            if int(client[0]) >= int(plans[mid]):
                left = mid+1
            else:
                right = mid-1
        print(mid)



    return answer

