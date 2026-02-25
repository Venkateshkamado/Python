l=[2,5,4,8,1,3]
le=len(l)
if l[0] > l[1]:
    maxi = l[0]
    maxi2 = l[1]
else:
    maxi = l[1]
    maxi2 = l[0]
for i in range(2,le):
    if l[i] > maxi:
        maxi2 = maxi
        maxi = l[i]

    elif l[i] > maxi2 and l[i] != maxi:
        maxi2 = l[i]

print(maxi2)