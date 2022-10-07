n = int(input())
start = 0
end = n
while True:
    mid = (start+end)//2
    if n < mid**2 :
        end = mid
    elif n>mid**2:
        start = mid
    else:
        print(mid)
        exit(0)
