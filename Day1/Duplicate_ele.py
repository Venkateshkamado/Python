l=[1,2,2,3,4,4,5,5]
nel = []
nol = []
for i in l:
    if i not in nel:
        nel.append(i)
    else:
        if i in nel:
            if i not in nol:
                nol.append(i)
print(nol)