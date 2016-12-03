updown = 0
leftright = 0
direction = 0
compass = ['N', 'E', 'S', 'W']

with open('input.txt') as f:
  instructions = f.readline().rstrip('\n').split(', ')

for inst in instructions:
  move, dist = inst[0], int(inst[1:])
  if move == 'L':
    direction = (direction - 1) % 4
  elif move == 'R':
    direction = (direction + 1) % 4
      
  if compass[direction] == 'N':
    updown += dist
  elif compass[direction] == 'E':
    leftright += dist
  elif compass[direction] == 'S':
    updown -= dist
  elif compass[direction] == 'W':
    leftright -= dist
    
print(abs(updown) + abs(leftright))