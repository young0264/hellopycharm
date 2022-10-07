t = int(input())
cute=0
notcute=0
for i in range(t):
    x = int(input())
    if x==1:
        cute+=1
    else:
        notcute +=1
if cute < notcute:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")