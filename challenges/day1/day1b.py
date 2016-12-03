updown = 0
leftright = 0
direction = 0
compass = ['N', 'E', 'S', 'W']
points = []
found = False

with open('input.txt') as f:
  instructions = f.readline().rstrip('\n').split(', ')

for inst in instructions:
  move, dist = inst[0], int(inst[1:])
  if move == 'L':
    direction = (direction - 1) % 4
  elif move == 'R':
    direction = (direction + 1) % 4
    
  for i in range(0,dist):
    if compass[direction] == 'N':
      updown += 1
    elif compass[direction] == 'E':
      leftright += 1
    elif compass[direction] == 'S':
      updown -= 1
    elif compass[direction] == 'W':
      leftright -= 1
  
    pointString = str(leftright)+','+str(updown)
    if pointString in points:
      found = True
      break
    else:
      points.append(pointString)
      
  if found == True:
    break
    
print(pointString, abs(updown) + abs(leftright))