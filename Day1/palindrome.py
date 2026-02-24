word = "madam"
rev = ""

l = len(word)

for i in range(l - 1, -1, -1):
    rev = rev + word[i]

if(word==rev):
    print("Palindrome")
else:
    print("Not a Palindrome")