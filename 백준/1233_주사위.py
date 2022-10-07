from collections import defaultdict
a,b,c = map(int,input().split())
dic = defaultdict(list)
arr = []
for i in range(1,a+1):
    for j in range(1,b+1):
        for t in range(1,c+1):
            key = sum(sorted([i,j,t]))
            #key = ''.join(list(map(str,s)))
            if not dic[key] :
                dic[key] = 1
            else: dic[key] += 1

max_value = max(dic.values())
#print(dic)
for i in dic.keys():
    if dic[i] == max_value:
        print(i)
        exit(0)
