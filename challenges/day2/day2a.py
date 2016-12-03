keypad = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
vertpos, horzpos = 1, 1

with open('input.txt') as f:
  for line in f:
    for i in line:
      if i == 'L' and horzpos > 0:
        horzpos -= 1
      elif i == 'R' and horzpos < 2:
        horzpos += 1
      elif i == 'U' and vertpos > 0:
        vertpos -= 1
      elif i == 'D' and vertpos < 2:
        vertpos += 1

    print(keypad[vertpos][horzpos], end='')
print()