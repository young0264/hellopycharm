# 시간복잡도를 한번 더 생각할 수 있었던 문제ㅣ
n = int(input())
m = int(input())
s = input()
shape = 'IOI'
i = 0
answer = 0
cnt = 0
while i < m-1 :
    if s[i:i+3] == shape:
        cnt += 1
        i += 2
        if cnt == n:
            answer += 1
            cnt-= 1
    else:
        cnt = 0
        i+=1
print(answer)


#shape = 'IO'*n +'I'
#for i in range(0,s_len-len(shape)+1):
#    if s[i:i+len(shape)]==shape:
#        cnt += 1
#print(cnt)
