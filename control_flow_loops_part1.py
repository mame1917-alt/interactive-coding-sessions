#Loops are code blocks that are going to run multiple times.
#We are going to learn or relearn about two different kinds of loops:
#WHILE loops, and FOR loops.

#Lets start with the WHILE loop:
count = 0 #Dont worry about this for now
while count < 5: #while keyword, followed by a CONDITION: a statement that evaluates to True or False
    print(count)
    count = count + 1
#A while loop is going to execute AS LONG AS the condition is false.
#AS soon as the condition becomes True, it will no longer run
#That means a while loop will run zero, one, two, ... infinitely many times

#The typucal structure of a while loop:
#0. Initialization: the condition must be equal to something
#1. Inside the loop, something will happen to the condition.
#if the condition is never changed, the loop will run forever

#A very commoin use case for a while loop is to WAIT until some condition becomes True:
user_input = " "  #Initialization
while user_input == " ":
    user_input = input("please enter something: ")
print("You entered" + user_input)

    #Lets use a while loop to process a to do list:
to_do = ["Laundry","Dishes","Yard cleaning","dog walking"] #intialization:
while len(to_do) != 0:
    item = to_do.pop() #removiung the last item of a list, and returns it:
    print("Now im doing this: " + item)
#The skill that we are going to practice, and that is important for reading code is called
#TRACING a loop:
#Understanding, at each iteration 0, what is item equal to? "dog walking"
#What is to_do equal to? ['laundry','dishes','yard cleaning']
#What is len(to_do) equal to? 3
#So is this while loop going to run again?

#One small detour:
#Let me tell you about f_strings:
my_age = 39
my_name = "Marlee"
my_school = "CU Boulder"
greeting = "Hello, I'm" + my_name + str(my_age) + "and I go to " +  my_school
print(greeting)
#This works, nothing wrong with that but:
#It's ugly and long to write
#and I need to remember to convert any non-str variable into string before I can add it.
better_greeting = f"Hello, I'm {my_name}, I'm {my_age} and I go to {my_school}"
print(better_greeting)

#Remember a while loop is something that checks if a conditio is True.

#What is FOR loop?
#If is something that ITERATES on an object, and runs as many times as the number of elements
#in the object

for number in [1,2,3,4,5]: #it starts with the keyword FOR
#then it names a variable, called the "STEP" variable
#then an ITERABLE: soemthing that contains a number of elements
#WHile the for loop is running, 
#The STEP variable is going to take the value of all the elements
#in the iterable, one by one
    print(f"The number is {number}")

for letter in "Marlee"
print(letter)

#here, the loop is just printing the element. We can do more complicated things

list_of_numbers = [1,2,3,4,5,6]
for number in list_of_numbers:
    squarte = number **2
    print(f"The Square root of {number} is {square}")

#Lets practice TRACING that loop:
#iteration #, number , square
#FIrst iteration, 1 ,1
#Second, 2 ,4
#Third, 3,9

#Lets amp up the difficulty slightly:
#here, we were nto saving them anywhere
#Lets build another for loop that stores the squares in a new list

list_of_numbers = [1,2,3,4,5,6]
list_of_squares = [] #this is what will contain our square numbers once we calculate them
for number in list_of_numbers:
    square = number ** 2
    list_of_squares.append(square) #Append adds to the existing list, modifying it in place.

#Iteration #, number ,square, list-of_squares
#First, 1,1,[1]
#Second, 2,4,[1,4]
#third, 3,9 [1,4,9]

#After the loop concludes:
#Final, 6,36 [1,4,9,16,25,36]
print(list_of_squares)
print(list_of_numbers)

#Lets say you really do not understand how the loop is working:
#add a print statement tracking exactly whats going on
list_of_numbers = [1,2,3,4,5,6]
list_of_squares = [] #this is what will contain our square numbers once we calculate them
for number in list_of_numbers:
    square = number ** 2
    list_of_squares.append(square) #Append adds to the existing list, modifying it in place.
    print(f"Current iteration: number is {number},square is {square}, list_of_squares is {list_of_squares}")

#Very common use case for a for loop: Accumulate something.
list_of_numbers = [4,8,15,23,42,9]
#I want to know what all these numbers sum to
#This is what you get when you add them all, one by one.
total = 0 #very important! otherwise we cannot start adding. 
for number in list_of_numbers:
    total= total + number
    print(f"The sum of {list_of_squares} is {total}")
#Lets trace this:
#Iteration #, number , total
#First, 4, 4
#Second, 8, 12
#Third, 15, 27
print(total == sum(list_of_numbers))

#Now lets do a for loop that gets us the MAXIMUM value in a list of numbers
list_of_numbers = [4,-3,9,-7,14,52]
max_value = -99999999999
for x in list_of_numbers:
    if x > max_value:
        max_value = x

        #If x is SMALLER than our current max, we don't care. We move on

#Iteration #, x , max_value
#First, 4, 4 #max_value equal to 4 because its greater than -9999999
#Second, -3, 4 #the max value doesnt go away, so 4 is still bigger
#Third, 9, 9
#FOurth -7, 9 
#Fifth 14, 14
#Sixth 52, 52
print(max_value)
print(max_value