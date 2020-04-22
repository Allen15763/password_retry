
password = 'a123456'
chance = 3
while chance > 0:
	text = input('Please type your password: ')
	if text == password:
		print('log in success!')
		break
	else:
		chance = chance -1
		print('wrong password,', chance, 'times left')




