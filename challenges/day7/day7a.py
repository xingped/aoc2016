with open('input.txt') as f:
	count = 0
	for line in f:
		intls, outtls = 0, 0
		inbrackets = False

		for i in range(0,len(line)-4):
			if line[i+3] == '[':
				inbrackets = True
				i += 4
			elif line[i+3] == ']':
				inbrackets = False
				i += 4
			elif line[i] == line[i+3] and line[i+1] == line[i+2] and line[i] != line[i+1]:
				if inbrackets:
					intls += 1
				else:
					outtls += 1

		if outtls > 0 and intls == 0:
			count += 1

	print(count)