def large_num(*a):
    maxi = a[0]
    for i in a:
        if maxi<i:
            maxi=i
    return maxi
x=large_num(1,2,3,46,7,8,9)
print(x)
