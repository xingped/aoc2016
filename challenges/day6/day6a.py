message = ''
freq = []

with open('input.txt') as f:
	for line in f:
		if(len(freq) == 0):
			for i in range(0,len(line)):
				freq.append({})

		for i,c in enumerate(line):
			if c in freq[i]:
				freq[i][c] += 1
			else:
				freq[i][c] = 1

	for col in freq:
		message += max(col, key=col.get)[0]

print(message)