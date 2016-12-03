inputs = []
anchor = 0
with open('input.txt') as f:
  for line in f:
    if anchor == 0:
      inputs.extend(([],[],[]))
    
    column = 3
    for num in line.split(None,2):
      inputs[len(inputs)-column].append(int(num))
      column -= 1
    
    anchor = (anchor+1)%3
    
count = 0
for case in inputs:
  if case[0] + case[1] > case[2] and case[0] + case[2] > case[1] and case[1] + case[2] > case[0]:
    count += 1
    
print(count)