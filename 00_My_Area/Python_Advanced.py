# Loops

#refresher on lists, tuples and ranges

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

