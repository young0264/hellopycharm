import sys

stack_l = list(sys.stdin.readline())
stack_r = []
n=int(sys.stdin.readline())
for i in range(n):
    x=sys.stdin.readline().split()

    if x[0]== 'L' and stack_l :#스택ldl True(값이있으면)
        # 스택이 비어있는 경우는 따로 계산을 안해도되나
      #  if stack_l==0:
       #     stack_l=0
        stack_r.append(stack_l.pop())
    elif x[0]=='D'and stack_r :
        stack_l.append(stack_r.pop())
    elif x[0] == 'B'and stack_l:
        stack_l.pop()
    elif x[0] == 'P':
        stack_l.append(x[1])

#print(''.join(stack_l + list(reversed(stack_r))))
print(''.join(stack_l+list(stack_r[::-1])))
#print(stack_l)
#print(stack_r)