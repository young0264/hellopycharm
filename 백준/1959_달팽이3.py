#하. Log(N)시간복잡도가 어케나오지
r , c = map(int,input().split())
curve = 0
location = 0,0
x,y = 1,1   #현재위치
mo = min(r,c)
skin = 0
if mo %2 ==0:
    skin = (mo//2)-1
else:
    skin = min(r,c)//2
r, c = r-2*skin, c-2*skin
curve += 4*skin
x , y = x+skin , y+skin #현재위치 초기화
#2100000000
if r == 1:
    y += (c-1)
elif c == 1:
    curve += 1
    x += (r-1)
elif r == 2:
    curve += 2
    x += 1
elif c == 2:
    x += 1
    curve += 3

print(curve)
print(x,y)