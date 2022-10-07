#n = input()
#cnt = 0
#i=0
#for j in range(1,1000000):
#    if n[i:] in str(j) :
#        if n[i:]==str(j):
#            i+= 1*(len(str(j)))
#            cnt = j
#            if i == len(n):
#                break
#        else:
#            i+=1
#            cnt = int(j)
#            #print(j)
#            if i == len(n) :
#                break
##########
n = input()
cnt = []
i = 0
while True:
    i +=1
    l_i = str(i)
    while len(l_i) > 0 and len(n) > 0:
        if n[0] == l_i[0] :
            n = n[1:]   #한자리에서의 구현이
        l_i = l_i[1:]   #숫자는 증가하고 각자리수까지 살펴보는것
        print(n)
    if len(n) == 0:
        print(i)
        break

#####
# a='1'일때
# a[0] = 1 , a[1] = index밖, a[1:] = 빈 슬롯,len(a[1:]) =0, a[1:] == ''



