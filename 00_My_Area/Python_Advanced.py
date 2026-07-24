# Loops

#refresher on lists, tuples and ranges (iterables)
#iterables are a type of objects you can loop over (one value at a time)

#lists are not immutable (can update individual values) and can have repeated values
my_list = ['Tom', 'Dick', 'Harry']

#tuples are immutable (cannot update individual values) and can have repeated values
my_tuple = ('Tom', 'Dick', 'Harry')

#you can use indexing to extract individual values from lists and tupels
#indexing starts at 0, and you can use negative indexing to index from the end
#you can also use a colon (:) to define a first and last value to extract, to pull a range of values
print(my_list[0])
print(my_tuple[-1])
print(my_list[0:1])

#you can update individual entries in a list, but the same operation would error in a tuple
my_list [0] = 'Frank'
print(my_list) # now returns Frank, Dick, Harry

#you can delete individual entries in a list using the del keyword
#syntax is del list_name [index]
del my_list [2]
print(my_list) # now returns Frank, Dick (Harry has been deleted)

#use the in operator to check if a value is in a list (Bool)
print('Dick' in my_list) # returns True as Dick is in the list

#you can also the list() keyword to convert an exisiting iterable into a list
my_string = 'William'
my_new_list = list(my_string)
print(my_new_list) # as each charecter in a string can be iterated on, returns W,i,l,l,i,a,m

#the len() operator can be used on a list to retrive the number of entires in it
print(len(my_new_list))

my_range = range(1, 11, 1)
#ranges generate a range object, which contains a start value, end value (non inclusive) and a step value
#syntax is range(start, stop, step) - step defaults to 1

#if you were to convert a range object to a list, it returns all values in that range
print(list(my_range)) # returns 1,2,3,4,5,6,7,8,9,10


#advanced list functions


#you can nest lists inside lists
my_nested_list = ["red", "green", ["light blue", "dark blue"]]

#you can then provide an index for the outer and inner list to retrive an entry
print(my_nested_list[2][1]) # returns 'dark blue'

#you can assign list entries to new variables in turn, known as unpacking lists
employee_481 = ['Matthew', '36', 'Security Consultant']
name, age, job_title = employee_481 # this created 3 new variables and assigns them list entires in turn
print(f'{name} is {age} and works as a {job_title}')

# using an astrisk (*) assigns all remaining list values to a variable
employee_481 = ['Matthew', '36', 'Security Consultant', 'Legend']
name, age, *job_title = employee_481 # job_title is now assigned a list containing the last two values
print(f'{name} is {age} and works as a {job_title}')

# .count() can be used to count how many times a value occours in a list
# syntax is .count(value)
my_list = [1,2,3,4,5,3]
my_list.count(3) #returns 2

# .append() is a method used to add a new entry to a list
my_list = [1,2,3,4]
my_list.append(5)
print(my_list) # now returns [1,2,3,4,5]

#if you were to use .append() to add a list to another list, it would nest it a single entry
my_list = [1,2,3,4]
my_second_list = [5,6,7,8]
my_list.append(my_second_list)
print(my_list) # returns [1,2,3,4,[5,6,7,8]]

# .extend() prevents this nesting, adding each value as indivual list entries
my_list = [1,2,3,4]
my_second_list = [5,6,7,8]
my_list.extend(my_second_list)
print(my_list) # returns [1,2,3,4,5,6,7,8]

# .insert() is used to add a new entry to a list at a certain point (without overiding an exisiting entry)
# syntax is .insert(index of insert, new entry value)
my_list = [1,2,3,4,5,6]
my_list.insert(3,"midpoint") #note the insert index pushes the value that was there up by one
print(my_list) #returns [1,2,3,midpoint,4,5,6]

# .remove() deletes a single value from a list - passing the value as the argument
#  syntax is .remove(value to be deleted) - note this will only delete the FIRST OCCURRENCE OF THE VALUE
my_list = [10,20,30,40,50]
my_list.remove(40)
print(my_list) # now returns [10,20,30,50]

# .pop() deletes a single value from a list - passing the index as the argument
# if no index is specified, it removes the last entry from the list
my_list = [1,2,3,4,5]
my_list.pop(0)
print(my_list) # now returns [2,3,4,5]

# .clear() deletes all entries in a list
my_list = [1,2,3,4,5]
my_list.clear()
print(my_list) # returns an empty list

# .sort() sorts a list numerically
my_list = [2,4,1,3,5]
my_list.sort()
print(my_list) # returns [1,2,3,4,5]

#this also works on letters
my_list = ['a','c','b']
my_list.sort()
print(my_list) # returns [a,b,c]

# sorted() also sorts a list, but creates a new list rather than updating the existing
# syntax is .sorted(existing list to be sorted)
my_list = [1,3,2,5,4]
my_sorted_list = sorted(my_list)
print(my_sorted_list) # note my_list is unchanged 

#you can use the key variable for .sort() to modify how they are sorted
my_list = ['red', 'yellow', 'blue']
my_list.sort(key=len) # this sorts a list be value length
print(my_list) # returns ['red', 'blue', 'yellow']

# you can also use the key variable for sorted()
# in this example, its sorted by absolute value (polarity is ignored)
my_list = [-10,-5,0,5,10]
my_sorted_list = sorted(my_list, key=abs)
print(my_sorted_list) # returns [0,-5,5,-10,10]

# the reverse varibale can also be used by .sort() and sorted() reverse the indexing of a list
my_list = [1,2,3,4,5]
my_list.sort(reverse=True)
print(my_list) # returns [5,4,3,2,1]

# .reverse() also reverses the indexing of a list (1st becomes last etc)
my_list = [1,2,3,4,5]
my_list.reverse()
print(my_list) # now returns [5,4,3,2,1]

# .index() is used to find the index of the first occurance of a value
my_list = [1,2,3,4,5]
my_list.index(4) # returns an index of 3

# advanced tuple functions
# reminder - tuples are immutable (cannot be changed after creation)

#you can convert an exisiting value into a tuple
my_string = "Hello World"
my_tuple = tuple(my_string)
print(my_tuple) # returns ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')

#like lists, you can search for a value in a tuple using the 'in' operator
my_tuple = (1,2,3,4,5)
4 in my_tuple #returns True (Bool check)

#you can also unpack tuples into varibables like lists
my_tuple = ('Matthew', 36, 'Security Consultant')
my_name, my_age, my_job = my_tuple
print(f'my name is {my_name}, I am {my_age} years old and work as a {my_job}')
#you can also use the * operator to unpack all remaining values into a variable

# as with lists, tuples can use .count() and .index() functions
# as there immutable, update functions such as sort do not work on tuples
# however, .sorted() can be used as it generates a new object
my_tuple = (1,3,2,5,4)
my_sorted_tuple = sorted(my_tuple)
print(my_sorted_tuple)

#Loops

#Loops repeat code blocks a set number of times
#a "for" loop does this by assigning each value in an iterable to a temp variable (e.g. food) in turn, then executing
#syntax is - for (temp varaible) in (iterable): {indented code block}

my_list = ['pizza', 'curry', 'burgers']

for food in my_list:
    print(f'my favourite food is {food}') # this prints the sentence for each entry in my_list

#you can also iterante through other iterables such as strings using for loops
my_string = "EIEIO"
for char in my_string:
    print(f'the next character is {char}')

#for loops can also be nested (iterates again using a second iterable on each value in the first iterable)
my_fruit_list = ['orange', 'apple', 'banana']
my_animal_list = ['otter', 'red panda', 'alpaca']

for fruit in my_fruit_list:
    for animal in my_animal_list:
        print(f'your randomly generated passwords are {fruit}{animal}') #this would print orangeotter, orangeredpanda, orangealpaca, appleotter, appleredpanda, etc)

# while loops repeates a code block until the condition=False
# in this code, the while loop repeats until guess does not equal my password is False (conditions are used for the outputs)
# this will return "try again!" until the right password is guessed

my_password = "password1234"
guess = "0000"

while guess != my_password:
    guess = input("enter guess: ")
    if guess != my_password:
        print("try again!")
    else:
        print("you got it!")

# break can be used to terminate a loop e.g. if a certain condition is met

pokemon = ['charmander', 'bulbasaur', 'squirtle']

for starters in pokemon:
    if starters == 'bulbasaur':
        break
    print(starters) #this returns charmander only, as the loop is terminated at the next iteration

# continue skips a single loop iteration e.g. if a certian condition is met

pokemon = ['charmander', 'bulbasaur', 'squirtle']

for starters in pokemon:
    if starters == 'bulbasaur':
        continue
    print(starters) # this returns charmander and squirtle, as bulbasaur is skipped

#an else clause can be placed after a for or while loop, which only triggers if the loop is not terminated by a break statement

name = 'Matthew'

for letter in name:
    if letter.lower() == 'a':
        print(f'your name ({name}) does  contain an a')
        break
else:
    print(f'your name ({name}) does not contain an a')


# revision: ranges are used to generate a sequence of integes - range(start,stop,step) - the stop argument is NOT inclusive
for number in range(10): 
    print(number) # this would contain 0,1,2,3,4,5,6,7,8,9 (one argument defaults start to 0 and step to 1)

# ranges can return values in reverse order by using a negative step value
for number in range(10,0,-1):
    print(number) # this returns 10, 9, 8 .... 1

# you can also create a list of integes using the by using list

numbers = list(range(1,10,2))
print(numbers) # returns [1, 3, 5, 7, 9]



# enumarate() can be used to return iterables in a list and their corresponding index as a series of tuples
names = ['Tom', 'Dick', 'Harry']
print(list(enumerate(names))) # note like a range, an enumurate object needs to be converted into a list to print its contents - returns (0,'Tom'), (1,'Dick'), (2,'Harry')

# enumarate() can be used in loops to track the index of iterables
names = ['Tom', 'Dick', 'Harry']
for index, names in enumerate(names):
    print(f'Name {names} has an index of {index}') # returns Name Tom has an index of 0... and so on

# you can also declare a START index for enumarate by providing it as an argument, if not present it defualts to 0 - syntax is enumurate(LIST,START)

names = ['Tom', 'Dick', 'Harry']
print(list(enumerate(names, 1))) # this now returns (1, 'Tom') etc

# zip() can be used to merge two lists in a series of tuples so they can be iterated through in parellel
employees = ['John','Frank','Ian']
employee_IDs = [3012, 3013, 3014]

for employee, employee_ID in zip(employees, employee_IDs): # zip will create an object with a series of tuples ('John', 3012)... etc
    print(f'{employee} has an Employee ID of {employee_ID}') # returns John has an Employee ID of 3012... etc


# list comprehensions create a new list from an exisiting iterable (often a list), allowing concise code as conditions can be applied when creating the new list
# syntax is - [expression(new item added to new list derived from the exisiting item iterable)  for  item(temp name for item in exisiting iterable)  in  iterable(i.e an exisiting list)  if  condition(optional filter condition e.g !=0)]

meter_readings = [22,46,-10,102,-134]
postive_meter_readings = [reading for reading in meter_readings if reading > 0] #note the new item and existing item are the same, as we are just adding exisiting list entries to a new list if a condition is met
print(postive_meter_readings) # creates a list of only positve meter readings

#this example does squares all numbers in a list, note no optional condition is used and the existing iterable item is modified in the new item expression

numbers = [5,10,15,20]
numbers_squared = [num**2 for num in numbers]
print(numbers_squared) # returns the square of all numbers

# filter () can also be used to create a new list from an exisiting iterable, creating a new list containing only the entries that pass a filter function
# syntax is filter (function, iterable)

numbers = [4,36,157,1000,2,34,295,943]

def is_big_number(number):
    return number > 100

big_numbers = list(filter(is_big_number, numbers))
print(big_numbers) # returns all numbes over 100

# map() can be used simular to filter(), creating a new list by performing a function on all values in an exiting iterable
# map() uses it provided funciton to change the input iterable and create a new value in the created list, rather than using that funciton to filter new list entries
# syntax is the same - map(function,iterable)

numbers = [10,20,30,40,50]

def add_one(number):
    return number+1

numbers_plus_one = list(map(add_one, numbers))
print (numbers_plus_one) # returns [11, 21, 31, 41, 51]

#sum() simply provides the sum of all numbers in an iterable
numbers = [12,35,6,25,12]
print(sum(numbers)) # returns 90

#you can also give sum a START value, which inflates the eventaul sum by an artifical START value (i.e. it doesn't start at 0)
numbers = [12,35,6,25,12]
print(sum(numbers,10)) # now returns 100

# lambda functions are a different type of functions that have no assigned name, they are useful for embedding funtions within higher funcitons without having to assign them a name
# syntax is lambda argument(s): expression
# best practice is to keep lambda funcitons reserved for simple logic within higher functions such as map() or filter()

numbers = [10,20,30,40,50]

numbers_plus_one = list(map(lambda number: number + 1,numbers)) # note a arbitery name of "number" is chosen for the expressions pulled in turn from the numbers list

print (numbers_plus_one) # also returns [11, 21, 31, 41, 51] without having to create a named function as before



#Dictionaires

# Dictionaries store key : value pairs, syntax is {key:value}
# Dictionaries entries are immuntable and each key must be unique (values can be repeated)
my_dictionary = {'Name' : 'John',
                 'Age' : 40,
                 'Hair':  'Brown'}

# alternative syntax

my_dictionary = dict([('Name', 'John'), ('Age', 40), ('Hair', 'Brown')])

# to retrive a value, you need to call the dictionary and its key - syntax is dictionary[key]
my_dictionary['Name']

# you can alternativly  use .get() to retrive values - dictionary.get(key)
my_dictionary.get('Name')

# the advantage of .get() method is a default value can be returened if the key does not exist
my_dictionary.get('Height', 'Key does not exist') # This returns 'Key does not exist' as there is no key called Height

# to update a value, simply add an assigment (=)
my_dictionary['Name'] = 'Fred'

# .keys() can be used to create an view object that lists all keys in a dictionary
my_dictionary.keys() # returns "dict_keys(['Name', 'Age', 'Hair'])"

# .values() does the same for all values in a dictionary
my_dictionary.values() # returns "dict_values(['John', 40, 'Brown'])"

# .items() creates an object listing all key-value pairs in a dictionary
my_dictionary.items() # returns "dict_items([('Name', 'John'), ('Age', 40), ('Hair', 'Brown')])"

# .clear() can be used to empty a dictionary
my_dictionary.clear()

# .pop removes a specific key:value pair and returns its value (by declaring that pair's key)
my_dictionary.pop('Age') # returns 40 and deletes the key:value pair 'Age':40

# .popitem() removes and returns the last inserted key:value pair
my_dictionary.popitem() # returns and deletes 'Hair':'Brown' as it was the last inserted key:value pair

# .update({}) can be used to update a multiple key:value pairs in a dictionary - if the key already exists it will update the value, if it does not it will create a new entry
# note the updates need to be nested in ({})
my_dictionary.update({'Age':30, 'Height':"192cm"}) # 'Age' now has a value of 30, and a new key:value pair of 'Height':'192cm' has been added


# By default, when you loop on dictionaries it iterates on the keys only

car_prices = {'Tesla' : 50000,'Skoda' : 40000, 'Ford' : 30000}

for car in car_prices:
    print(car) # returns Tesla Skoda Ford

# To loop on values, you need to create a view object containing all dictionary values using .values()

for price in car_prices.values():
    print(price) # now returns 50000 40000 30000

# To use loop on both keys and values in a dictionary, you can use a view object containing both using .items()

for car_name, car_price in car_prices.items():
    print (f'the {car_name} costs {car_price}') # returns 'the Tesla costs 50000.....'

# .update() can be used in a loop to modify a dictionaries values, in this example 20% is taken off each price

car_prices = {'Tesla' : 50000,'Skoda' : 40000, 'Ford' : 30000}

for car_name, car_price in car_prices.items():
    car_prices.update({car_name:int(car_price*0.8)})

print(car_prices) # car_prices now returns {'Tesla': 40000, 'Skoda': 32000, 'Ford': 24000}

# as with lists, enumerate() can be used to assign an integer to each key value pair when working on them in loops

for car in enumerate(car_prices):
    print(car) # returns (0, 'Tesla') (1, 'Skoda'), (2, 'Ford') - each key has been assigned an integer to form a tuple

# or they can be seperated in the loop (not in enumarate objects, the index comes first)

for index, car in enumerate(car_prices):
    print(f'{car} has an index of {index}') # returns "Tesla has an index of 0....""

# you can also use enumerate with values rather than keys using the .values() method

for index, price in enumerate(car_prices.values()):
    print(index, price) # returns 0 40000 etc








