def number_pattern(n):
    
    output = ''

    if type(n) != int:
        return "Argument must be an integer value."

    elif n < 1:
        return "Argument must be an integer greater than 0."

    else:
        for number in range(1,n+1):
            output += str(number) + ' '
        
        return output.strip()       

print(number_pattern(10))

