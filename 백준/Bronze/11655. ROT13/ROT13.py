n = input()
answer = []
for x in n:
    if x == ' ':
        answer.append(x)
    elif x.isdigit():
       answer.append(x)
    else:
      new_x = ord(x) + 13
      if x.islower():
        if new_x > ord('z'):
          new_x = new_x - ord('z') + ord('a') - 1
      elif x.isupper():
        if new_x > ord('Z'):
          new_x = new_x - ord('Z') + ord('A') - 1
      answer.append(chr(new_x))
print(''.join(answer))