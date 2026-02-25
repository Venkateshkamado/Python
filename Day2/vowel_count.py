def vowel_count(x):
    vowels = ["a","e","i","o","u"]
    count = 0

    for i in x.lower():
        if i in vowels:
            count += 1

    return count