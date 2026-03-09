#Base discount function

def apply_discount(price,discount):

    discount /= 100
    return (price * (1 - discount))
    

print (apply_discount(100,50))



