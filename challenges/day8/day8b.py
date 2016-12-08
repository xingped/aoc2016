display = [[0]*50 for i in range(6)]

with open('input.txt') as f:
	for line in f:
		inst = line.split()
		if inst[0] == 'rect':
			xy = inst[1].split('x')
			for y in range(0,int(xy[1])):
				for x in range(0,int(xy[0])):
					display[y][x] = 1
		elif inst[0] == 'rotate':
			if inst[1] == 'row':
				row = int(inst[2].split('=')[1])
				amt = int(inst[4]) % 50
				overflow = display[row][50-amt:50]
				for i in reversed(range(amt,50)):
					display[row][i] = display[row][i-amt]
				display[row][0:amt] = overflow
			elif inst[1] == 'column':
				col = int(inst[2].split('=')[1])
				amt = int(inst[4]) % 6
				overflow = []
				for i in range(6-amt,6):
					overflow.append(display[i][col])
				for i in reversed(range(amt,6)):
					display[i][col] = display[i-amt][col]
				for i in range(0,amt):
					display[i][col] = overflow[i]

	for i in range(6):
		print(display[i])