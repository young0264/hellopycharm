n = int(input())
m = int(input())
lights = list(map(int,input().split()))
answer = []
answer.append(lights[0])
answer.append(n-lights[-1])
for i in range(m-1):
    x = (lights[i+1]-lights[i])
    if x%2 ==0:
        answer.append(x//2)
    else:answer.append((x//2)+1)
print(max(answer))
