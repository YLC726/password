password = '6969'
x = 1
test = input('請輸入密碼:')

if test != password:
	while x < 3:
		print('密碼錯誤!還有',3 - x,'次機會')
		test = input('請輸入密碼:')
		x = x + 1
	print('密碼錯誤超過3次，請15分鐘後再來!')
else:
	print('密碼正確')