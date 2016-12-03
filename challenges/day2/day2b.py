keypad = [
  [None, None, 1, None, None],
  [None, 2, 3, 4, None],
  [5, 6, 7, 8, 9],
  [None, 'A', 'B', 'C', None],
  [None, None, 'D', None, None]
]
vertpos, horzpos = 2, 0

with open('input.txt') as f:
  for line in f:
    for i in line:
      if i == 'L' and horzpos > 0 and keypad[vertpos][horzpos-1] != None:
        horzpos -= 1
      elif i == 'R' and horzpos < 4 and keypad[vertpos][horzpos+1] != None:
        horzpos += 1
      elif i == 'U' and vertpos > 0 and keypad[vertpos-1][horzpos] != None:
        vertpos -= 1
      elif i == 'D' and vertpos < 4 and keypad[vertpos+1][horzpos] != None:
        vertpos += 1

    print(keypad[vertpos][horzpos], end='')
print()