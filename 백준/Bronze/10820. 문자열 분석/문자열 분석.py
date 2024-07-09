while True:
  try:
    answer = [0]*4
    words = input()
    for w in words:
      if w.islower():
        answer[0] += 1
      if w.isupper():
        answer[1] += 1
      if w.isdigit():
        answer[2] +=1
      if w == ' ':
        answer[3] += 1
    print(*answer)
  except:
    break
