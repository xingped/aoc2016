import re

with open('input.txt') as f:
	for line in f:
		sector = re.search(r'^([a-z\-]*)-(\d+)\[([a-z]{5})\]$', line).groups()
		d = {}
		for char in sector[0]:
			if char.isalpha():
				if char in d:
					d[char] += 1
				else:
					d[char] = 1
		
		z = sorted(d.items(), key=lambda a: a[0])
		z = sorted(z, key=lambda a: a[1], reverse=True)
		topfive = ''.join([e[0] for e in z[0:5]])
		
		if topfive == sector[2]:
			test = ''
			for i, c in enumerate(sector[0]):
				if c.isalpha():
					test += chr(((ord(c)-97+int(sector[1])) % 26) + 97)
				else:
					test += c

			if 'pole' in test:
				print(test+', '+sector[1])
				break