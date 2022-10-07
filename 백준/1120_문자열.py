#a가 b의길이보다 작거나 같다.
#길이의 차이만큼 b의앞에꺼를 a붙이거나 뒤에껄 a에붙여서 for문을 돌려본다.
a,b = map(str,input().split())
la,lb = len(a),len(b)
c = len(b)-len(a)+1

def f(arr1,arr2):
    cnt = 0
    #문자열 두개를 비교해서 다른값리턴
    for i in range(lb):
        if arr1[i] != arr2[i]:
            cnt +=1
    return cnt

ans = 10**5
for i in range(c):
    arr = b[:i] + a + b[la+i:]
    ans = min(ans,f(arr,b))

print(ans)











#ans = 0
#c = len(b)-len(a)
#ex1,ex2='',''
#res1,res2 = 0,0
#if not c:
#    for i in range(len(a)):
#        if a[i] != b[i]:
#            ans+=1
#else:
#    ex1 = b[0:c]+a
#    ex2 = a+b[-c:]
#    for i in range(len(b)):
#        if ex1[i]!=b[i]:
#            res1+=1
#            print(i)
#        if ex2[i]!=b[i]:
#            res2+=1
#    ans = min(res1,res2)
#print(ex1,ex2)

#print(ans)

