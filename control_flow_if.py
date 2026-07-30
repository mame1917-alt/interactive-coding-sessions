#Control flow is a term describong all the tools in Python that govern 
#whether, when, and how much/often a block of code is going to run
#Up until now, every line that we were writing was running.

#First up: CONDITIONAL LOGIC
#This is what governs whether a block of code is going to be executed

my_name = "Marlee"
my_gender = "Female"

if my_gender == "Female": 
    #A CONDITIONAL LOGIC block always starts with if
    #Followed by a CONDITION
    #A condition is a statement that will evaluate to True or False
    #the line ends with a colon
    #Then the line below, you start an indented block:
    #This indented block describes the line of code that will run
    #ONLY if the condition evaluates to True
    #For the most simple conditional logic block, that is all you need. 
    #A block with just one IF is binary: Either the block gets executed (if CONDITION is True)
    #Or it isnt (if CONDITION is false)
    print("Hello Ms " + my_name) 
    #Soemtimes the world is more complicated. Theres more than one possibility.
    #Thats where you can add some bells and whistles to your conditional block
    #using keywords elif and else


elif my_gender == "Male":
    #Elif is short for else if
    #it describes a second possible outcome
    #That is ONLY going to be checked if the previous conditions evaluated to False
    #It's sequential: we sytart at the top
    #We check if the first condition is True,
    #if it is True, we end here
    #if it is False, we check the second condition
    #WE can have zero, one, or many elif statements
    #Allowing you to check additional specific statements
    print("Hello Mr " + my_name)
elif my_gender == "Non-Binary":
    print("Hello" + my_name)
else: #Then, at the bottom, after all the elif statements (if any)
    #WE can have the "else" block. The else block means:
    #If all conditions turned out to be False,
    #heres what you should do.
    print("Hello" + my_name + ", how should we address you?")
    #if there is no else statement, nothing happens when all the other conditions evaluate to false

#A very common GOTCHA with conditional logic block:
#Conditional logic blocks are very common inside functions:
#They allow you to have functions that have a different behavior as a function of their inputs:

def status_checker(age):
    #We want this function to return the status of the user
    #as a function of the age that they specify
    if age >= 13:
        return "You are a teenager"
    elif age >= 18:
        return "You are an adult"
    elif age >= 4:
        return "You are a child"
    elif age >= 2:
        return " You are a toddler"
    else:
        return "You are a baby"
#Lets test our status checker function
status_checker(1) #You are a baby
status_checker(3) #You are a toddler
status_checker(9) # You are a child
status_checker(14) #You are a teenager
status_checker(39) #You are a teenager, because the conditional logic was true at the first statement

def correct_status_checker(age):
    #We should simply flip the first two conditions:
    #Statements are now ordered from Most to Least restrictive
    #Meaning if a statement is True, all the other statements that follow are also True.



    if age >= 18:
        return "You are a adult"
    elif age >= 13:
        return "You are a teenager"
    elif age >= 4:
        return "You are a child"
    elif age >= 2:
        return " You are a toddler"
    else:
        return "You are a baby"

    #If a conditional Logic statement is not behaving as epxected,
    #you should always check that the conditions are in order

    #What happens when you have multiple conditions that you want to check
def can_legally_drink(country, age):
        #the answer depends on the country and age
        #To do that we can nest conditional logic blocks
        if country == 'USA':
            #then inside the block, we handle the other condition
            if age >= 21:
                return 'You can legally drink in USA'
            else:
                return "You cannot legally drink in the USA"
        elif country == 'Canada':
         if age >= 19:
            return "You can legally drink in Canada"
        else:
            return "You cannot legally drink in Canada"

        elif country == "France":
        if age >= 16:
            return "You can legally drink in France"
        else:
        return "You cannot legally drink in France"
         else:
            return "Country not recognized"

can_legally_drink("France, 18")

#Could we writw this differently? Yes

#When you have a simple condition, you. can write a conditional logic block
#in a single line: that's called the "TERNARY OPERATOR"
age = 20
status = 'Adult' if age >= 10 else "Minor"
#VALUE_IF_TRUE if CONDTION else VALUE_IF_FALSE

#trick 1: WHen you have a simple comndition, you can write a conditional logic block
#in a single line: that's called the TERNARY OPERATOR

#Second trick, very useful and very common:
#A use case for conditional logic blocks is when you need to output one value
#Depending on another value:
#Lets say I want to output the currency of a country, depending on the country name:
# 
def get_country_currency(country_name):
            if country_name == "France":
                return "Euro"
            elif country_name == "USA":
                return "US Dollar"
            elif country_name == "Canada":
                return 'Canadian Dollars'
            #many lines like this
            else:
                return 'unknown country'
#Instead, a better solution: (dictionary)
country_currencies = {
    "USA": "US Dollars",
    "France": "Euro",
    "Canada" : "Canadian Dollars",
    "UK":"British Pounds",
    "Japan":"Yen"}

country_currencies["Canada"]
        #Achieves the same goal as conditional block
        #But it only works if you want to match the same variable to different possible values
        
#One small caveat:
country_currencies["Iran"]
country_currencies.get("Iran", "Country not found")