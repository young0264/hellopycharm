#A:65~90 / a:97~ () 40 41
틀림
num = list(input())
alphabet = ''
x = ''
for i in range(len(num)-1,-1,-1):
    if 65<=ord(num[i])<=90:
        alphabet += num[i]
    elif ord(num[i])<40 or ord(num[i])>41:
        x += num[i]

print(alphabet[::-1]+x)
