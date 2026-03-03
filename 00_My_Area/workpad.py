#basic print funtion (what is being printed must be in round brackets)
print ("hello Dave")
#can print multiple values by seperating with commas (Python auto adds a space)
print ('Tom', 'Dick', 'and Harry')


#basic maths with answers output via the print function
print(1+2) #addition
print(5-1) #subtraction
print(5*2) #multiplication
print(6/2) #division
print(5**2) #raise to a power


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


#strings (cont.) - strings are immutable, once declared to a variable they cannot be edited and instead must be reassigned

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