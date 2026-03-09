
def apply_discount(price,discount):
    
    if type(price) != float and type(price) != int:
        return ("The price should be a number")
    
    if type(discount) != float and type(discount) != int:
        return ("The discount should be a number")
    
    if price <=0:
        return ("The price should be greater than 0")
    
    if discount < 0 or discount > 100:
        return ("The discount should be between 0 and 100")

    else:
        discount = discount/100 * price
        return (price - discount)
    
print (apply_discount(50, 0))



