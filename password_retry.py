
password = 'a123456'
chance = 3
while chance > 0:
	chance = chance -1  #每一次輸入密碼都消耗一次
	text = input('Please type your password: ')
	if text == password:
		print('log in success!')
		break
	else:
		print('wrong password,')
		if chance > 0:
			print(chance, 'times left')
		else:
			print('Please contact customer service')





