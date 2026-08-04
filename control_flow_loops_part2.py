#You can consider that "Advanced topics" in loops

#One thing I said is that, in a for loop, the thing that we are looping over:
#for x in the_thing_we_are_looping_over is called ITERABLE
#An ITERABLE means: something we can unpack into distinctive elements

#We've seen some of them:
#Lists are iterable:
fruits = ['banana','apple','mango']
for f in fruits:
    print(f)

#WE've also seen that strings are iterable:
my_word = "Supercalifragilistic"
for letter in my_word:
    print(letter)
    #When you loop over a string, you are getting the letters one by one

#Dictionaries are iterable: 
my_info = {"name": "Marlee", "age":"22","city":"Boulder"}
for info in my_info:
    print(info). # I am getting the keys of the dictionary one by one

#how would I print both the key and the value?
for info in my_info:
    value = my_info[key]
    print(f"The key is {key} and the value is {value}")

    #If i want the value associated with the key "name":
    print(my_info["name"])

#There is an even better way that I'm showing you so that you can recognize it:
my_info.items() #this is giving me ech of the key value pairs in succession
#Th ebest news is? We CAN ITERATE on that!

for (key,value) in my_info.items():
    print(f"The key is {key} and the value is {value}")

#Much simpler example of unpacking
fruits = ["banana","apple","mango"] #this list contains three elements
my_first_fruits, my_second_fruits, my_third_fruit = fruits
print(my_first_fruits)

fruits = ["banana","mango","apple"]
#I want to write a loop that prints me:
#Fruit 1: banana
#Fruit 2: mango
#Fruit 3: apple

#The first function is called enumerate():
for (index, item) in enumerate(fruits):
    #When instead of iterating on the ITERABLE directly 
    #WE use enumerate(ITERABLE), we are getting both the index and the element at each loop
    print(f"The element at position {index} is {item}")

#Final one for today:
#lets say we have multiple lists that are somehow connected to each other
lists_of_goods = ["pickle","pepper","cherry"]
lists_of_tastes = ["sour","spicy","sweet"]
#here we might want to print: "a pickle is sour","a pepper is spicy"...
#There is a way of connecting, zipping, multiple iterables together

for (food, taste) in zip(lists_of_goods, lists_of_tastes):
    #At each iteration, we are getting on element of each list,
    #unpacked into their respective step variable
    print(f"A {food} is {taste}")

#What if we havethree lists?
list_of_colors = ["green","red","red"]

#It is not more complicated

for (food, taste,colors) in zip(lists_of_goods, lists_of_tastes, list_of_colors):
    #At each iteration, we are getting on element of each list,
    #unpacked into their respective step variable
    print(f"A {food} is {taste}")

    #Lets talk about range()
for i in [1,2,3,4,5]: #i is the STEP VARIABLE, [1,2,3,4,5] is the ITERABLE
    print(i) #i is going to take, in turn, the value of each of the elements in the iterable.
#Now imagine we want to get all the numebrs from 0 to 1000:
#Writing the loop the old way:
for i in [0,1,2,3,4,5,1000]: # a bit of a pain to write.
#so enter range()
#range is a function that creates an iterable for you that you can loop on
#range takes three arguments: start,stop, step
#start is also optional, and defaults to 0
#step is optional, and defaults to 1
for i in range(1001): #All the numbers between 0 and 1001 excluded
    print(i)

    #start,stop, step should remind you of slices:
my_list= [0,1,2,3,4,5,6,7,8,9,10]
my_list[0:4]
my_list[::2]

for i in range(0,1000,2):
    print(i)

    #All there is to know about rangea: a convenient way of getting an interable of numbers to loop on
    #The final thing on loops is something called LIST COMPREHENSIONS
#Lets say I want the square of all the numebrs between 0 and 9.
#Lets write a loop that iterates over numbers between 0 and 9,
#take the square of each of them
#and stores them in a list called my_squares
my_squares = [] #intialize and empty list to store the squares
my_numbers= [1,2,3,4,5,6,7,8,9] #the iterable
for i in my_numbers:  #outside of the loop, assign each of the elements of my number to step variabke i
   square = i ** 2
   my_squares.append(square) 
print(my_squares)

#or you could do this
my_squares = [] #intialize and empty list to store the squares
my_numbers= [1,2,3,4,5,6,7,8,9] 
for i in range(10):
    my_squares.append(i ** 2)
print(my_squares)

#This task,creating a new lust from an existing iterable, is EXTREMELY common in python
#Thats what a shortcut called LIST COMPREHENSION is doing:
#Could have done the same job by typing:
my_squares= [ i **2 for i in range(10)]
#A list comprehension is surrounded by square brackets, becausee we are creating a list
#then, you see an EXPRESSION: i **2. This defines how the step variable is going to be modified
#to create the elements of the list
#Finally, you the loop itself: for STEP_VARIABLE in ITERABLE. Note there is no colon here.
print(my_squares)

my_list= [x.upper() for x in "quentin"]
print(my_list)

#One final thing on LIST COMPREHENSION
#We can add, after the (for STEP VARIABLE in ITERABLE) an optional IF statement,
#that filters the elements of the list
my_filtered_squares = [ i ** 2 for i in range(10) if i ** 2 < 30]
#Only add to the list if the sqaures are less than 30:
my_filtered_squares

#very common use case for this filter:
paths = ["data.csv","report.pdf","summary.csv","image.png","notes.txt","data2.csv"]
#lots of file names of different types
#Lets say I just want to keep the csv files
my_csv = [i for i in paths if i .endswith(".csv")] 
print(my_csv)

#How could I write a for loop that would the same job:
my_csv = []
for path in paths: 
    if path.endswith(".csv"):
        my_csv.append(path)
print(my_csv)

