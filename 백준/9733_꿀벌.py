crr = ['Re', 'Pt', 'Cc', 'Ea', 'Tb', 'Cm', 'Ex']
arr = []
while True:
    try:
        brr = list(map(str, input().split()))
        if not brr:
            break
    except EOFError:
        break
    arr = arr+brr
    # print(arr)

length = len(arr)
dic = dict()

for a in arr:
    dic[a] = dic.get(a, 0) + 1

for c in crr:
    if c in dic:
        res = round(dic[c] / length, 2)
        # print(c, dic[c], res)
        print(c, dic[c], format(dic[c]/length,".2f"))

    else:
        print(c, 0, '0.00')
print('Total', length, '1.00')
