l = [1, 3, 6, 5, 2, 10]

max_val = l[0]

for i in range(len(l)):
    if max_val < l[i]:
        max_val = l[i]

print(max_val)