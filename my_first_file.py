print("hello world")
print(2+2) #here nothing gets executed right now when you hit enter up here
#how can I run this code?
#Two ways:
#1. You can put the caret on the line and press shift + enter
    #It is going to send the line to a REPL and run it
#2 The second way is to run the file\
    #Send the entire content of the file to Python, and all the lines will be executed in sequence. 
    #Do this by pressing the run button at the top right of the central panel.
    #You will want to do this once you've finished writing your script.

#Reminder 1, we can create variables in python and assign a content to them:
my_name = "marlee meinerth"
print(my_name)
#Lets send line 14 (print) to the REPL

#Four big types of data in python
this_is_an_integer = 10
this_is_a_float = 3.14 #number that has a decimal part
this_is_a_string = "Hello world"
this_is_a_boolean = True 

#print using the print() function
print(this_is_an_integer)
print(this_is_a_float)
print(this_is_a_string, this_is_a_boolean) #we can print multiple things at once, separated by a comma
print(my_non_existing_variable)

#print() is a Function. A function is something that takes between 0 and many arguments, and that has specific behavior.
    #it is an "action"

#You can print:
#A value
print(3.14)
#A variable:
print("marlee meinerth")
#A expression, something that has not been calculated yet:
    #Reminder: expressions are calculated inside out
print(2+2)

#SKILL: When reading code, try to always understand what is going to happen and in which order. 
# "Tracing the code"; understanding the steps the machine is taking 

print(this_is_an_integer)
print(this_is_an_integer + 5 ) #Can you trace this?
# 1. Read the value contained inside the variable, "this is an integer"
# 2. Do the operation, here,a sum, between this is an integer (10) and 5
# 3. Print the result of this operation

#How do you figure out the type of a variable?: 
what_is_this = type(this_is_an_integer)
print(what_is_this)

what_is_that = type(3.14)
print(what_is_that)

#CALCULATIONS
print(2 +3)
print(2 + 3*5)
print((2+3)*5) # PEMDAS
print(1+2)
print((1+2) ==3) #Double equal is a logical comparison, checking if the elements on the right and on the left have the same value
# logical comparisons always return a boolean, True or False
print(0.1 +0.2)
print((0.1 + 0.2)== 0.3)
#Floating point error. Do not expect float operations to be exact
#What can you do?
my_rounded_addition = round((0.1 + 0.2), 1) 
    #This function takes two arguments: the element to be rounded, the digits of precision required
    #The way to deal with floating point error is to use round 

round(3.14) #functions can have non-compulsory arguments, default arguments. For round, ndigit is equal to 0 if not specified

#Logical comparisons: 
print(3 == 5)
print(3 > 5)
print(3< 5)
print(3 >= 5)
print(3 <= 5)

# You can combine logical comparisons using 'and' or 'or'
condition_1 = True
condition_2 = True
condition_3 = False
condition_4 = False
print(condition_1 and condition_2)
#AND only returns True when ALL the conditions are True
print(condition_1 or condition_2) #True
print(condition_1 or condition_3) #true
print(condition_3 or condition_4) #False
#AND only returns true when all confitions are true
# OR returns True as long as one condition is True
print(True + True) #True are 1, False are 0
print(True == 1)
print(False == 0)
print(True * 5) #This is 5, because for Python true is one and false is zero
print(10/0) #Division error, you cannot divide by zero

#Lets do some string manipulations
#Calculations with strings
#when used with strings, the + is interpretted as a "concatenation operator", technical word for putting things next to each other
greeting = "Hello " + "World" #space after the hello and before last apostrophe is how to get space in between two words
print(greeting)

laugh = "ha" * 3
print(laugh)
#For Strings, the multiplication sign is interpretted as a repeat operation
#Be careful when mixing up different types, sometimes tolerated but often rejected and always confusing to read
very_complicated_laugh = 'ha' * ('hello' == 'hello') *3
print(very_complicated_laugh)

# How do we keep things simple? We make sure to convert variables before working with them
number = 42
is_this_a_number = "42"
print(number + 10) # 52
#If you attempt to add a number to a string, you will get an error
print(is_this_a_number + 10 ) #How do we solve this?
#Create a new variable with the apprepriate type:
now_this_is_a_number = int(is_this_a_number)
# int() turns something that is not a number into a number
print(now_this_is_a_number)
int('15') == 15
# What would I get if typed this?
int('fifteen') # you get an error
int("marlee") # you get an error
int(False) # This one works!

#One more example
my_age = 22
my_intro = "Hello, my name is Marlee and I am " + my_age

# my intro corrected
my_intro_corrected = "Hello, my name is Marlee and I am " + str(my_age)
print(my_intro_corrected)

float('3.14')


# str(), float(), int(), and bool() are functions
#that can turn an input into the desired type...assuming this is possible