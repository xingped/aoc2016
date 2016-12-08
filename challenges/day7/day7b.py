with open('input.txt') as f:
	count = 0
	for line in f:
		aba, bab = [], []
		inbrackets = False

		for i in range(0,len(line)-3):
			if line[i+2] == '[':
				inbrackets = True
				i += 3
			elif line[i+2] == ']':
				inbrackets = False
				i += 3
			elif line[i] == line[i+2] and line[i] != line[i+1]:
				if inbrackets:
					bab.append(line[i:i+3])
					if line[i+1]+line[i]+line[i+1] in aba:
						count += 1
						break
				else:
					aba.append(line[i:i+3])
					if line[i+1]+line[i]+line[i+1] in bab:
						count += 1
						break

	print(count)