# Classes are blueprints for creating objects, grouping together objects that share common behaviours/attributes

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# every class must have a function called __init__ (DOUBLE UNDERSCORES) which defines the data attributes each object created
# from that class possesses - e.g. name, breed, age etc


# the first parameter of _init- is always a refrence to the specific object being created
# convention is to call it self for clarity 

# in this example, dog_1 is the object that is passed to self - with attrubites being dog_1.name and dog_1.breed

dog_1 = Dog("Charlie","Border Terrier")

print(dog_1.name)
print(dog_1.breed)

# Once the class attrubities have been defined by __init__ - class methods (behaviours) can be defined using functions
# methods are accessed by using the dot notation (object_name.method_name)
# Note that you need to pass self to the function to enable it pull in object attributes

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f'{self.name} says woof woof!')

dog_2 = Dog("Maple", "Golden Doodle")

dog_2.bark()

# The attributes set above are INSTANCE ATTRIBUTES as they are unique for each object created from that class
# CLASS ATTRIBUTES which are common to all objects created from a class can also be set:

class Dog:

        Best_Pet = True
        
        def __init__(self, name, breed):
            self.name = name
            self.breed = breed

dog_2 = Dog("Maple", "Golden Doodle")

print(dog_2.Best_Pet) # resolved to True as it inherted it from the class as a CLASS ATTRIBUTE

print(Dog.Best_Pet) # as it belongs to the class, you can also access class attriutes by refrencing the class rather than an instance


# Special methods are methods/functions under the hood in python, examples include __init__ and __add__ (called under the hood when you use +)
# Also called dunder methods (double under i.e. __method__)

# Custom classes are classes the same as strings or floats (which have there own methods and how they handle special mehtods has been defined)
# What special methods such as __len__ do are pre-defined for built in classes e.g. for strings it retures the amount of charecters
# Custom classes does not know how to handle special methods - so there behaviour needs defining

class Book:
     def __init__(self,title,page_count):
          self.title = title
          self.page_count = page_count

book1 = Book("The Hobbit",800)

print(len(book1)) # returns error as len() has not been defined for the class Book
print(str(book1)) # returns default repesenation of book1 "__main__.Book object at 0x7daa4c79f4d0"

# to change the the behviour of special methods for a custom class, you need to define them in the class

class Book:
     def __init__(self,title,page_count):
          self.title = title
          self.page_count = page_count

     def __len__(self):
          return self.page_count

     def __str__(self):
          return f'This book is called {self.title} and has {self.page_count} pages'

book1 = Book("The Hobbit",800)

print(len(book1)) # now returns the page count (800)
print(str(book1)) # now returns "This book is called The Hobbit and has 800 pages"


# Sometimes you need to access or manage object attributes dynamically at runtime rather than statically in code
# getattr(object_name, 'attribute_name', 'optional_default_value') can be used to lookup attributes dynamically 
# The optional default value is returned if the attribute is not found

# The below example uses an input to lookup the desired attribute for car1

class Car:
     def __init__(self, make, colour):
          self.make = make
          self.colour = colour

car1 = Car("Skoda", "Red")

print(getattr(car1,'make')) # getattr retrives "Skoda"

attribute_name = input ("what attribute do you want to lookup: ")

print(getattr(car1, attribute_name, "not found"))

          
# you can use dir() to return a list of attributes an object has

class Car:
     def __init__(self, make, colour):
          self.make = make
          self.colour = colour

car1 = Car("Skoda", "Red")

for attribute in dir(car1):
     value = getattr(car1, attribute)
     print(f'{attribute}') # this returns all attributes one at a time

# setattr(object_name, 'value_name', 'value') can be used to create or update an attribute

setattr(car1, 'colour','Blue')
print(car1.colour) # colour has been updated to "Blue"

# hasattr(object_name, 'attribute_name') checks if an attribute exists (True or False)

print(hasattr(car1,'make')) # True

# delattr (object_name, attribute_name) deletes an attribute from an object

delattr(car1, 'make')
print(car1.make) # now returns "'Car' object has no attribute 'make'"