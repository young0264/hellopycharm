a= list(map(int,input().split(':')))
b= list(map(int,input().split(':')))
al=a[0]*3600 + a[1]*60 + a[2]
bl=b[0]*3600 + b[1]*60 + b[2]
res = bl-al
if res < 0:
    res += 24*60*60
h = res//3600
m = (res%3600)//60
s = res%60
print(str(h).zfill(2)+':'+str(m).zfill(2)+':'+str(s).zfill(2))
#print("%02d:%02d:%02d" % (h,m,s))
#'%0.2f'%number
