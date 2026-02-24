word = "venkatesh"

vow = ["a", "e", "i", "o", "u"]
count = 0

for i in word:
    if i in vow:
        count = count + 1

print(count)