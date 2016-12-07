import hashlib

m = hashlib.md5()

puzzle = 'wtnhxymk'
password = 'zzzzzzzz'
index = 0

while 'z' in password:
	while True:
		hash = hashlib.md5((puzzle+str(index)).encode()).hexdigest()
		index += 1
		if hash[0:5] == '00000' and int(hash[5], 16) < 8 and password[int(hash[5])] == 'z':
			password = password[:int(hash[5])] + hash[6] + password[int(hash[5])+1:]
			print(str(index-1)+' - '+password+', ('+hash[5]+','+hash[6]+')')
			break

print(password)