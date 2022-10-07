from decimal import Decimal

abc=['A+' ,'A0', 'A-','B+', 'B0', 'B-','C+','C0', 'C-',
       'D+', 'D0', 'D-','F']
grade =[4.3, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7,0.0]
n = int(input())
check=[]
fake=[]
for i in range(n):
       x = list(map(str, input().split())) #x의 인덱스값에 대응되는 다른배열의 값 출력
       locate = abc.index(x[-1])
       fake.append(int(x[-2]))
       check.append(grade[locate]*int(x[-2]))

res=((sum(check)/sum(fake)))

if (res*1000)%10 == 5 :
       res=res+0.01
       print(round(res,2))
else:
       print('%.2f'%res)