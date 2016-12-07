import hashlib

m = hashlib.md5()

puzzle = 'wtnhxymk'
password = ''
index = 0

while len(password) < 8:
	while True:
		hash = hashlib.md5((puzzle+str(index)).encode()).hexdigest()
		index += 1
		if hash[0:5] == '00000':
			password += hash[5]
			print(str(index-1)+' - '+password)
			break

print(password)