#basic print funtion (what is being printed must be in round brackets)
print ("hello Dave")
#can print multiple values by seperating with commas (Python auto adds a space)
print ('Tom', 'Dick', 'and Harry')


#create variables and their associated values e.g. time_zone = 'GMT'
#note: variable name cannot have spaces, cannot start with a number, cannot use python keywords, are case sensitive, and text values must be in quotation marks ('' or "") (strings)
time_zone='GMT'
name='John Smith'
age=35
print(time_zone)
print(name)
print(age)


#Basic data types in Python

my_integer = 10

my_float = 10.0

my_string = "hello world!"
#single or double quotation marks can be used to define a string (both quotation mark types treated the same)

my_boolean = True
#Boolean is either True or False (with capital first letter)

my_set = {5, 'red', 10.0}
#unordered collection of values that does not allow duplicaties (can be edited after creation - "mutable")

my_list = [5, 'red', 10.0]
#ordered collection of values that allows duplicaties (can be edited after creation - "mutable")

my_tuple = (5, 'red', 10.0)
#an ordered collection of values that allows duplicaties (cannot be editied after creation - "immutable")

my_dictionary = {'name':'John', 'age':35, 'job':'postman'}
#a collection of key-value pairs (e.g age-35) assigned to a variable (in this case "dictionary")

my_none = None
#special value which reperesents no value at all

my_range = range(1, 11, 2)
#creates a range of numbers (useful in loops etc), first value is the start number, second is the stop and third is the step between values
#my_range would retern 1, 3, 5, 7 and 9 (starts at 1, steps by 2 and ends at 10 (stop value is not inclusive)

#check the data type of a varible using the type() funtion
print (type(my_tuple))

#Do a Boolean (true or false) check to see if a value is (true) or is not (false) a certain data type using the isinstance() function
isinstance (my_string, str)


#strings - strings are immutable, once declared to a variable they cannot be edited and instead must be reassigned

#strings can span muliple lines by putting in or triple quotes ('''x''' or """x""") - prevents need to use \ to move to a new line
my_multiline_string = """hello
world
again!"""

#if there are quotation marks in the string, you can use the alternate type use to mark the start and end of the string
my_quote = "he said 'sorry'"
#or you can use an escape (\) before the quotation mark to identify its not the start or end of the string
my_quote_revised = "he said \"sorry\""

#the "in" operator can be use to check if combinations of charecters exist in a string (return bool True or False)
print('world' in my_multiline_string)

#the "len" oeprator can be used to check the length of a sting
print(len(my_multiline_string))

#each character in a string has a position called an index. The index is zero-based, meaning that the index of the first character of a string is 0
#To retrive a specific charecter in a string, you can use its index using square [x]
print(my_multiline_string[3]) 

#you can also use negative indexing to work your way back from the end of the string [-x]
print(my_multiline_string[-4]) 

#you can combine strings into a new variable using the "+" operator (concatenation/cat)
my_str_1 = 'red'
my_str_2 = 'lorry'
my_cat_str = my_str_1 + ' ' + my_str_2
print(my_cat_str)

#you can only cat strings, if you cat a non string value like an integer, you can convert into a string using the str() operator
mileage = 50000
my_cat_str_2 = my_str_1 + ' ' + my_str_2 + ' ' + str(mileage)
print(my_cat_str_2)

#you can combine strings and update an exising varible with the new value using the '+=' operator
full_name = 'Andy'
full_name += ' Jones'
print(full_name) # full_name variable is now Andy Jones

#interpolation: you can add variables directly into strings by using f-strings (formatted strings) - these are denoted by an f before the string starts and allow variables to be inserted within {}
#note you do not need to manually convert other data types such as integers into strings via the str() operator, this is done automatically by f-strings
my_age = 40
my_introduction = f'hello my name is {full_name} and I am {my_age} years old'
print(my_introduction)


#you can "slice" stings (extract a certain part of a sting) by declaring a start and stop index (start:stop)
#remember that the first letter is index 0, and the stop value is not inclusive (so will return up to the last letter before)
print(my_cat_str_2[0:3]) # this returns "red"

#if you omit the start or stop value, it defualts start to 0 and and stop to the end of the string
print(my_cat_str_2[:3]) # this also returns "red"
print(my_cat_str_2[3:]) # this returns the string starting after red

#you can also add a step permiter to the slice to extract for example each 2nd charecter (start:stop:step)
print(my_cat_str_2[0:3:2]) # this returns "rd"
#if you leave start and stop blank, and use -1 as the step, returns the whole string in reverse (::-1)
print(my_cat_str_2[::-1])


#python provides useful string functions, such as .upper() to convert a whole string to uppercase
my_new_string = 'hello dave'
my_new_string_uppercase = my_new_string.upper()
print(my_new_string_uppercase) # returns 'HELLO DAVE'

#.capitalize() converts the first letter of a string only to uppercase
my_new_string_capitalised = my_new_string.capitalize()
print(my_new_string_capitalised) # returns 'Hello dave'

#.title() convers the first letter of each word to uppercase (i.e. title case)
my_new_string_titlecase = my_new_string.title()
print(my_new_string_titlecase) # returns 'Hello Dave'

#.strip('x') returns a new string with the specificed leading and trailing charecters removed (if none declared removes whitespace only)
my_trimmed_string = my_new_string.strip('h')
print (my_trimmed_string) #returns 'ello dave'

#.replace('old, 'new') replaces specific charecter sequences within a string with a new value
my_amended_string = my_new_string.replace('hello', 'hi')
print(my_amended_string) # returns "hi dave"

#.split('x') breaks down a string into a list of strings, using the specificed value as the seperator (if none declared defaults to whitespace)
my_split_string_list= my_new_string.split()
print(my_split_string_list) # returns a list containing 'hello' and 'dave'

#.join() is used to join values in an iterable such as a list into a single string, seprated by a defiend value
# syntax is 'seperator'.join(my_iterable)
my_fixed_string = ' '.join(my_split_string_list)
print(my_fixed_string)

#.startswith('x') checks if a string starts with a specific prefix, returns a bool True or False
starts_with_hello = my_fixed_string.startswith('hello')
print(starts_with_hello) # returns True as "hello dave" starts with "hello"

#.endswith('x') does the same for the suffix
ends_with_hello = my_fixed_string.endswith('dave')
print(ends_with_hello)

#.find('x') searches a string for a substring, and returns the index of its first occurence (returns -1 if not found)
find_dave = my_fixed_string.find('dave')
print(find_dave) #returns an index of 6

#.count('x') counts the amoutn of times a substring appears in a string, and returns the total
count_dave = my_fixed_string.count('dave')
print(count_dave) # returns 1 as dave appears in the string once

#.isupper() returns a bool True if all charecters are uppercase, false if any are not
check_if_uppercase = my_fixed_string.isupper()
print(check_if_uppercase) # returns false as it contains lowercase charecters

#.islower() does the same bool check to see if all charecters are lowercase
check_if_lowercase = my_fixed_string.islower()
print(check_if_lowercase) # returns True as it contains all charecters are lowercase



#Numbers and Mathmatical operations

#reminder of basic maths with answers output via the print function
print(1+2) #addition
print(5-1) #subtraction
print(5*2) #multiplication
print(6/2) #division
print(5**2) #raise to a power

#if you use an integer and a float in arithmetic, the answer automatically converts to a float
my_integer_1 = 8
my_float_1 = 0.6
my_sum_1 = my_integer_1 + my_float_1
print(my_sum_1) # resolves to a float of 8.6

#modulo operator (%) returns the remainder when the value on the left is divided by the value on the right
my_integer_2 = 5
my_mod_sum = my_integer_1 % my_integer_2
print(my_mod_sum) # returns a remainder of 3

#floor division (//) divides two numbers (integer or float) and always rounds down to nearest whole integer
my_fd_sum = my_integer_1 // my_integer_2
print(my_fd_sum)

#float() function can convert a number in another format (int, string) into a float
my_float_2 = float(my_integer_2)
print(my_float_2) # returns a float of 5.0

#int() function does the same conversion into an integer
my_integer_3 = int(my_float_2)
print(my_integer_3) # returns a integer of 5

#round() can be used to round a float to defined number of decimal places (by default rounds to nearest whole integer)
my_float_3 = 9.62
my_rounded_float_1 = round(my_float_3) # rounds to nearest whole integer (10
my_rounded_float_2 = round(my_float_3, 1) # rounds to the nearest 10th an integer (9.6)
print(my_rounded_float_1)
print(my_rounded_float_2)

#abs() returns the absolute value of a number (removes the polarity of numbers, -5 becomes 5)
my_integer_4 = -10
my_abs_integer = abs(my_integer_4)
print(my_abs_integer) # returns 10

#pow() is an alternative way to raise to a power (**) when used with 2 variables
exp_sum_1 = pow(5, 2) # returns 25 (5**2)
print(exp_sum_1)

#using 3 variables is the same as raising the first value to the power of the second, then performing a modular calcuation with the result
exp_sum_2 = pow(5,2,10) #  returns 5 (5**2 = 25 | 25 % 10 = a remainder of 5)
print(exp_sum_2)

#you can apply a mathmatical operation to edit an exisiting varible using (+=) (-=) etc.
my_number = 10
my_number += 5
print(my_number) # my_number is now 15 [10 + 5]
my_number *= 2
print(my_number) #my_number is now 30 [(10 + 5) * 2]
#you can also use some augmented assignments on strings (+= and *=)
my_string_2 = 'hello '
my_string_2 *= 3
print (my_string_2) #returns 'hello hello hello)


#conditional statements and logical operators 

#comparison operators (returns bool true or false)
value_1 = 10
value_2 = 15
print(value_1 == value_2) # checks if values are equal (True or False)
print(value_1 != value_2) # checks if values are not equal
print(value_1 > value_2) # checks if value on left is greater than the value on the right
print(value_1 < value_2) # checks if value on the left is less than the value on the right
print(value_1 >= value_2) # checks if value on left is greater or equal to value on the right
print(value_1 <= value_2) # checks if value on left is less or equal to value on right

#the (if) keyword creates a conditional, which performs a check and executes a code block if the condition is true
#'if' conditions need to be terminated with a (:)
#the code block is defined using an single indent

age = 20
if age >= 18:
    print('you are an adult')

#the (else:) keyword can be used to define an code block to run if the condition is False
age = 15
if age >= 18:
    print('you are an adult')
else:
    print('you are a child')

#(elif) can be used to define a second condition, which is checked if condition 1 is False
#you can still follow with and (else:) code block, which will execute if both are False

age = 14
if age >=18:
    print('you are an adult')
elif age >=13:
    print('you are a teenager')
else:
    print('you are a child')

#you can use as many (elif) statements as you like
age = 6
if age >=18:
    print('you are an adult')
elif age >=13:
    print('you are a teenager')
elif age >=5:
    print ('you are a child')
else:
    print('you are a infant')





#note: you can use the 'pass' as a placeholder in a mandatory code block that will be defined later



