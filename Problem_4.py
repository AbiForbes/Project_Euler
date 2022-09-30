Number = 0
Number_string = ''
flag = True
Old_largest = 0

for i in range (100, 1000):
	for j in range(100, 1000):
		Number = i * j
		Number_string = str(Number)
	
		for k in range(0,int(len(Number_string)/2)):
			if Number_string[k] != Number_string[len(Number_string)-k-1]:
				flag = False
				
		if flag == True:
			if Number>Old_largest:
				print(Number)
				Old_largest = Number
		flag = True
