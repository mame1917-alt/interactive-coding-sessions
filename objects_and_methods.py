this_is_an_integer = 10
this_is_a_string = "Marlee"
type(this_is_an_integer)
type(this_is_a_string)

#After creating a variable in python, you can check all the things that
#are contained in that variable using the .dot in VScode. After you press the dot, it will reveal a 
#list of things contained in the object. 
# These things come in two flavors:
# PROPERTIES: signaled by the wrench icon, contains information. data.
# METHODS: described by a purple box. Describes all the actions that can be performed by the object.
print(this_is_an_integer.numerator) #10
print(this_is_an_integer.denominator) #1
this_is_an_integer.real
#PROPERTIES are describing the state of the object that we created.
another_integer = 5
print(another_integer)
#Can we check some properties of the string?
print(this_is_a_string) #No properties in there

#What is really useful are methods, allow us to DO stuff with the objects that we created. They are like a function in that
    # they can do things, but they are specifically attached (we say "Bound") to the object.

#Lets check out some methods of this is a string:
this_is_a_string.upper() #a method requires parentheses, because they are actions. They are like a function so you need
# to "call" them.
# All strings will have this method. All objects of a given type share the same methods.
this_is_a_string.lower()
this_is_a_string