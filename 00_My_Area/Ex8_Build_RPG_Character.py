def create_character(name, strength, intelligence, charisma):
    

    if not isinstance(name,str):
        return("The character name should be a string")
    
    if name == "":
        return("The character should have a name")
    
    if len(name) > 10:
        return("The character name is too long")
    
    if name.find(" ") != -1:
        return("The character name should not contain spaces")
    
    if type(strength) != int or type(intelligence) != int or type(charisma) != int:
        return("All stats should be integers")
    
    if strength < 1 or intelligence < 1 or charisma < 1:
        return("All stats should be no less than 1")
    
    if strength > 4 or intelligence > 4 or charisma > 4:
        return("All stats should be no more than 4") 
    
    if (strength + intelligence + charisma) != 7:
        return("The character should start with 7 points")
    
    STR = ('●' * strength) + ('○' * (10 - strength) )
    INT = ('●' * intelligence) + ('○' * (10 - intelligence) )
    CHA = ('●' * charisma) + ('○' * (10 - charisma) )


    return (f"{name}\nSTR {STR}\nINT {INT}\nCHA {CHA}""")
    

print(create_character('ren',4,2,1))