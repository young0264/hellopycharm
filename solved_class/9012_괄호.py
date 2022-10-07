import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    m = list(input())
    cnt = 0
    for i in m :
        if i=='(':
            cnt += 1
        elif i==')':
            cnt -= 1
        if cnt < 0 :
            print('NO')
            break
    if cnt > 0 :   #양수들
        print('NO')
    elif cnt == 0 :
        print('YES')

















#  for i in m:
#      if i == '(':
#          result += 1
#      elif i == ')':
#          result -= 1
#      if result<0 :
#          print("NO")
#          break

#  if result == 0 :
#      print ("YES")
#  elif result >0 :
#      print('NO')