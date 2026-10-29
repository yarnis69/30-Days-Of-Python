# Classes are blueprints for creating objects, grouping together objects that 
# share common behaviours/attributes

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# every class must have a function called __init__ (DOUBLE UNDERSCORES) which defines the attributes each object created
# from that class possesses - e.g. name, breed, age etc


# the first parameter of _init- is always a refrence to the specific object being created
# convention is to call it self for clarity 

# in this example, dog_1 is the object that is passed to self - with attrubites being dog_1.name and dog_1.breed

dog_1 = Dog("Charlie","Border Terrier")

print(dog_1.name)
print(dog_1.breed)

# Once the class attrubities have been defined by __init__ - class behaviours can be defined using functions
# Note that you need to pass self to the function to enable it pull in object attributes

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f'{self.name} says woof woof!')

dog_2 = Dog("Maple", "Golden Doodle")

dog_2.bark()
