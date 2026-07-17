def number_pattern(n):
    
    output = ''

    if type(n) != int:
        print("Argument must be an integer value")

    elif n < 1:
        print("Argument must be an integer greater than 0")

    else:
        for number in range(1,n+1):
            output += ' ' + str(number)
        
        print(output)
        

number_pattern(4)
