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