number = 600851475143

flag = True

while number > 1:
    for i in range (2,number):
        if number%i == 0:
            for j in range(2, i):
                if i%j == 0:
                    flag = False
                    break
            if flag == True:
                print (i)
                number = number/i
        flag = True        

    
                
