# Loops

#refresher on lists, tuples and ranges

my_list = ['Tom', 'Dick', 'Harry']
#lists are not immutable (can update individual values) and can have repeated values

my_tuple = ('Tom', 'Dick', 'Harry')
#tuples are immutable (cannot update individual values) and can have repeated values

#you can update individual entries in a list, but the same operation would error in a tuple

my_list [0] = 'Frank'
print(my_list) # now returns Frank, Dick, Harry

my_range = range(1, 11, 1)
#ranges generate a range object, which contains a start value, end value (non inclusive) and a step value
#syntax is range(start, stop, step) - step defaults to 1

#if you were to convert a range object to a list, it returns all values in that range
print(list(my_range)) # returns 1,2,3,4,5,6,7,8,9,10


