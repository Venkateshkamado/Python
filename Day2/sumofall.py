def sum_all(*a):
    sumofall=0
    for num in a:
        sumofall = sumofall + num
    return sumofall
x=sum_all(1,2,3,4,5,6,7,8,9,10)
print(x)