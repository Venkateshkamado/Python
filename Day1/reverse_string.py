word = "python"
rev = ""

l = len(word)

for i in range(l - 1, -1, -1):
    rev = rev + word[i]

print(rev)