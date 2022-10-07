s = int(input())

k=1
#res = s - k
while True:
    res = s-k
    if res >= k+1 :
        k += 1
        s=res
    else: break
print(k)