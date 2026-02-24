ex = "madam"
freq = {}
for ch in ex:
    if ch in freq:
        freq[ch] += 1 
    else:
        freq[ch] = 1
print(freq)