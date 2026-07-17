def number_pattern(n):
    
    output = ''

    if type(n) == int:

        for number in range(1,n+1):
            output += str(number) + ' '
        
        print(output)

    else:
        print("Argument must be an integer value")


number_pattern('a')
