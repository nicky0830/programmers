word = input()
alphabet = [0]*26
for w in word:
    diff = ord(w) - ord('a')
    alphabet[diff] += 1
print(*alphabet)