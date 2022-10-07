cnt = 0
while True:
    ans = 0
    cnt+=1
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    mok = V // P
    na = V % P
    ans += mok * L
    if na <= L:
        ans += na
    else:
        ans += L


    print("Case", str(cnt)+":", ans)
