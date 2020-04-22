
password = 'a123456'
chance = 3
while True:
	text = input('Please type your password: ')
	if text == password:
		print('log in success!')
		break
	else:
		chance = chance -1
		print('wrong password,', chance, 'times left')
		if chance == 0:
			print('bye')		
			break



