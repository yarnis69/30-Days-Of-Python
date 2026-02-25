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
#single or double quotation marks can be used to define a string

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