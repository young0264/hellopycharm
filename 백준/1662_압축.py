from bisect import bisect_left, bisect_right
a=['(','a','(','a','(','b',')','a',')','a',')']
a.sort()
print(a)
print(bisect_right(a,'b'))