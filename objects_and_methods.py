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

#What is stored inside these objects?
my_str.upper # Upper is a METHOD that is attached to all the objects of class str

my_str.endswith('orld') #returns true

#A method is like a functino, so it needs to be CALLED. How do we call a functionz?
 #We put () after it
 #Some objects have other things than methods: PROPERTIES
 #PROPERTIES are information about the object that was created. 
 my_integer.denominator #White wrenches are properties of the object
my_integer.numerator #DO we put parenthesis?  NO
#Properties are only meant to be read. They dont do anything.They just exist. 
#If something does not reuire any calculation to be given to you,
# and does not do anything, it is probably a property.  
# But to be sure: look at the icon.

# A few more methods for strings
#Strings contain a lot of methods because there are a lot of things that we can do with them. 
# We've already seen upper(), lower(), title(), capitalizing the first letter of each word.

my_sentence = "hello my name is marlee"
my_sentence.title()

# We have also seen 'endswith()'. Here are a few more:
lots_of_white_space = "       Marlee    "
lots_of_white_space.strip()

# Let me show you a practical example of how these methods can be useful
entry = "  marlee.meinerth@colorado.edu      "
    #This could be something someone entered into a form
    # I want to check if this person has a .edu email address
is_it_edu = entry.endswith("edu")
is_it_edu # it is false because of the whitespaces
stripped_entry = entry.strip()
is_it_edu_for_real = stripped_entry.endswith('edu')
is_it_edu_for_real
    #Is it a Boolean?
type(is_it_edu_for_real)
        #Final thing on this: we could write is_it_edu_for_real more clearly:
        #Here, we have created a new variable with strip(), and then used the 
        #endswith() method on this new variable. But we can skip this step:
is_it_edu_for_real  = entry.strip().endswith('edu')
        # entry.strip returns a string, meaning we can directly call the method
        #endswith() on this newly created string.

#This is called CHAINING. You call methods on an object that is returned by another method. 

#Common errors with methods and properties 
entry.shout() #Attribute error: No attribute shout()
#You try to call a method that does not exist on the object
price = 12
price.numerator()  # TypeErrorL int object is not callable, You call functions. 
#When you use parenthese(), it is calling something
type(price.numerator) #Numerator is a property of the integer 12, stored into price
#It contains an integer,which is 12
#But an integer does not do anything. It is not a function or a method.
#You cannot call it. Thats what the 'not callable'  is telling you.
#The error: attemtpting to call a property. You can only call a method inside an object

#Lets do some more exploration:
price.is_integer  # This is a method, purple box, and it is an action that we are doing
#What will happen if I run this line?
    #We need the parenthese to call the method, otherwise it is not doing anything.
price.is_integer()

#So far, we've seen four big types of objects:
#str,float, int, bool
#In python, you are often going to create 
#Let me show you one object tht is going to solve a problem we had before

from decimal import Decimal

#What is Decimal? It is a factory for manufzcturing a new kind og object: Decimal Objects
#Tp create str, you only needed to put quotes around something
#to create a float or an int, you just needed to type float or an int
#To create a boolean, you just needed to type True or False, or have a logical comparison

#To create Decimal Objects, we are going to use the Decimal thingie we jst imported
a = Decimal(".1")
#WE have created a new decimal objct, with the value .1
type(a)
b = Decimal(".2")
type(b)
print(.1 + .2). #What we get? A floating point error
#This is because, by default, Python represents floats with a limited number of zeros
print(a + b) #If you print the sum of two Decimal objects, you get an excat representation
#That's the problerm that Decimal is solving. 
a.  #If you reach into a Decimal object with a dot, you are going to see alot
#of new methods and properties