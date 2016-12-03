inputs = []

with open('input.txt') as f:
  for line in f:
    inputs.append([])
    for num in line.split(None,2):
      inputs[len(inputs)-1].append(int(num))
    
count = 0
for case in inputs:
  if case[0] + case[1] > case[2] and case[0] + case[2] > case[1] and case[1] + case[2] > case[0]:
    count += 1
    
print(count)