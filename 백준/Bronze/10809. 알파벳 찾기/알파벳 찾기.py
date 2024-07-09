word = input()
alphabet = [-1]*26
for i,w in enumerate(word):
    place = ord(w) - ord('a')
    if alphabet[place] == -1:
      alphabet[place] = i
print(*alphabet)