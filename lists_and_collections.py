#Talk about collections. COLLECTIONS are objects designed to hold other objects inside them.
#They are like bags of different kinds

#First Lists
        #A list is an ordered collection of items.
        #It is created using square brackets
my_empty_list = [] #This is a list that doesnt contain anything
type(my_empty_list) #A list
    #Lists contain other objects

my_favorite_numbers = [1,2,3,4,5] #List of integers
print(my_favorite_numbers)


#Lists can contain other elements 
my_favorite_colors = ['red','blue','green'] #This is a list of strings
my_favorite_decimals = [3.14,2.718,1.618] #This is a list of floats
my_favorite_booleans = [True, True, False] #Lists can contain repeated elements

#Lists can contain different elements of different kinds 
my_favorite_things = ["red",3.14, False]

#You can put anything you want into a list, even other lists!
my_mixed_list = [False, ["blue", 19], ["red", False],3.14]
#Dont be surprised, lists are very flexible. You can put a lot of things in them.

#Lists are objects meaning....
    #They contain properties and methods

#Lets see some methods of lists
my_favorite_colors.append('yellow') # ['red','blue','green']
#This line above did not print anything.
print(my_favorite_colors) #it contains yellow in the list now

#The method 'append' is SUPER differnt from all the other methods that we saw before, on strings for instance
#Because it CHANGED the object dirently. It mutated the original object.
#Lets refresh our memories
my_string = "marlee"
my_string.upper() #If i run this, it prints a string in upper case
print(my_string) #The original string is still in lower case
#In technical terms, the methods COPIES the original object, changes it, and returns 
#the copy.The original never changed.

#This is because strings are 'immutable'. Once created, their content will not change.
#The only way to make changes to a string is to create a new one with a different content

#Back to lists: lets see how methods affect them
my_favorite_colors #Now contains ['red','blue','green','yellow']
print(my_favorite_colors)\
#I am going to add the append method to add color pink
a = my_favorite_colors.append('pink')
#after I run this line?
print(my_favorite_colors)
#the method mutated the original list.The contents was chnaged directly by the method.
#But then what is inside of a?
print(a) #When you are working with a method that mutates the original,
#it will typically not return the original. It will simply do something on the original,
#and return none


#VERY CONFUSING, will not be on exam but worth knowing 

#Lets say we dont like the fact that everytime we are adding things to my favorite colors it changes 
#the original
my_original_colors = ['pink','purple']
#I want to add a color to this list but not modify the original
my_updated_colors = my_original_colors #I want this to be my backup
#Now I can add something to my updated colors, and my original colors
my_updated_colors.append('orange')
print(my_updated_colors) #Sweet, we added a new color
#Now what of my original colors?
print(my_original_colors)
#It prints the list with orange in it
#This is because lists are mutable so when you give a list a different names.
#it still points to the same list, rather than creating a copy of the list
#If you dont want that, you need to use the copy() method to create a copy of the list
my_original_colors.copy()


#Back to less confusing things
#Other methods with lists:
my_favorite_colors #['red','blue','green','yellow','pink']

#What if you want to remove an element of the list
#You can use a method called 'pop'. Pop is going to remove the last element of the list
#and returns it to you
removed_color = my_favorite_colors.pop()
#What wil be the content of my favorite colors
#the pop wil remove last element of the list and will place pink into removed color
print(my_favorite_colors) #['red','blue','green']
print(removed_color) #pink

#What if i rerun this line?
removed_color = my_favorite_colors.pop() #It will remove yellow from the list
#returns it to us in the removed color 

#Something new with lists: it you run the same command multiple times, the behavior
#will change. The list is being mutated, so you are not going to get the same results

#What happens if you dont assign the popped color?
my_favorite_colors.pop() #List now contains 9'red','blue','green']

#This is behavior that we have seen before: if a function returns something
#and we dont catch it into a variable, it falls into the terminal.

#Lists are ORDERED, meaning you can reach into them at a specific position
#and grab the content

my_favorite_names = ['Quentin','Zoe','Mathilda']
#Lets say I want to read what is at the beginning of that list?
#If you want to get an element, you can use an operation called INDEXING
#Indexing is: yo uput square brackets after the list, and use the INDEX of the 
#element that you want to grab:

print(my_favorite_names[1]) #Zoe. R starts counting from 1, python from 0.
# 0 returns the first element, 1 the second, 2 the third
print(my_favorite_names[0]) #Quentin

#What happens if you index [3]?
print(my_favorite_names[3]) #returns an error.

#lets continue our discussion of INDEXING
#WE can also use NEGATIVE indices:
print(my_favorite_names[-1]) #-1, reads the last value

print(my_favorite_names[-2]) # the second to last value

#WE can also do something called SLICING to grab multiple values from a list:
my_favorite_numbers = [1,2,3,4,5,6,7,8,9,10]
#Indexing again first:
my_favorite_numbers[2] #Getting to the 0,1,2: thir value of the list
#SLICING NOW:
#The syntax for slicing is [start:stop:step]. lets see what it means:
my_favorite_numbers[0:3:1]
#This means the values between the first and the fourth (excluded), and all of them
#More examples
my_favorite_numbers[1:6:1] #All valyes between the second and seventh (excluded) 
#and all of them
my_favorite_numbers[3:8:1] #All values between the fourth and eigth (or ninth excluded)
my_favorite_numbers[0:6:2] # All values between the firstm and seventh, going by 2

#When you are slicing, you can omit some arguments:
my_favorite_numbers[0:3] #By default, step is one (if ommitted)
#This is equivalent to [0:3:1]
#What about this?
my_favorite_numbers[1:] #All of the numbers starting from one
#Both end is ommitted (so it defaults) to the 'until the end')
#and step is ommitted (so it defaults to one)
my_favorite_numbers[:4] #Start is ommitted (so it defaults to zero, beginning),
#stop is 4 (meaning until 4th elemetn, excluded), step is ommitted so 1:
my_favorite_numbers[::2] #Start is ommitted (so zero), stop is ommitted (so until)
#the end, and step is 2: Every other value in the entire list

#Practice Slicing:
my_favorite_numbers[2:7:4]

#Cool trick for reversing a list
my_favorite_numbers[::-1]

#Want to see something cool?
my_name = "Marlee Meinerth"
my_name_but_mirrored = my_name[::-1]
my_name_but_mirrored # a string is an ordered collection of characters
#so you can slive it like a list
my_name[0:4]

#So far, we learned that:
#1) lists are MUTABLE, meaning we can modify their content using methods.
#2) lists are ITERABLE,meaning we can select a subset of their content using slices

#Lets put these two things together!
my_favorite_names #["Quentin",'Zoe',"Mathilda"]
#How could I replace quentin with adam
my_favorite_names[0] = 'Adam' #We are indexing the first element of the list, 
#and assigned the value 'Adam' at that position. 
my_favorite_names #WE have mutated the list

#WE can do the same thing with slices
my_favorite_names[1:] #This is slicing ['Zoe',"Mathilda"]
my_favorite_names[1:] = ['Eve', 'Joshua']
my_favorite_names # We can use slicing and indexing to read or update
#the content of a list

#Bonus question: Can we used indexing or slicing to update the content of a string
my_name[0] = "z"
#Strings are NOT mutable
#If you want a new string, you need to create a new string

#Back to a few list methods:
my_favorite_names.pop() # removes the last element of the list
my_favorite_names.append('Joshua') #Add this element at the end of the list
#Pop and append can take an additional argument: the POSITION!
my_favorite_names.pop(0) #This will pop the first element 
my_favorite_names.insert(0, 'Adam')
#All of these methods are modifying the original list. Not returning a copy of the list.
#Lets try one more:
my_favorite_names.reverse() 
#It returns nothing: It is changing the order of the original list


#Lists are collections of ordered items.
#Dictionaries are collections of key: value pairs.

#Lets start with an example:
my_friends_age = {'Nick':40, 'Sam': 35, 'Juan': 37}
#Note the syntax: Curly brackets, containing key:value pairs, separated by commas.

#Dictionaries can have different kinds of values:
my_information = {'name': "Marlee", 'age':39, 'hobbies':['coding','skiing','birding']}
#here you have the key 'name" that contains a string value,
#the key 'age' that contains int value
# the key 'hobbies' contains a list value

#What about the keys in a dictionary? What can they be?
#They are typically int or str. The most important rules:
    #They have to be UNIQUE (only one key must have a given name)
    #and they have to be IMMUTABLE.

#How do you use dictionaries?
#We can also reach inside them to see the values. That again called "INDEXING"
#For a list, it is ordered, so we index with numbers. 
#What do we index with when you have a dictionary?

my_friends_age['Nick'] #how do I get nicks age?
#I use square brackets to index, and I give the key for which I want to see the value

#What will I get if I type this?
my_information['hobbies']

#Dictionaries, like lists, are mutable. We can update them!
#lets say my friend Nick just celebrated his birthday
#How do I update his age?
my_friends_age["Nick"] = 41 #You reach into the dict at the desired key and you assign a new value to it
my_friends_age

#Lets try another example.
#Can I change my name to 'Quentin Andre'
my_information['name'] = 'Quentin Andre'
my_information
#name is the key that we would need to identify in order to change the actual names 

#We can add new keys to a dictionary
#I want to add ym job to my information
my_information['job title'] = 'marketing prof'
my_information
#We can use indexing to:
# 1) Read the value of an existing key
# 2) Update the valye of an existing key
# 3) Create a key with a given value

#Since dictionaries are OBJECTS....they have METHODS
#First useful method: get()
#If you index a dictionary with a value that does not exist, what happens?
my_information['address']
#If you accidentally check for a value that does not exist, you will get a KeyError
#A better way to check if a key exists is to use the method get()
quentin_address = my_information.get('address')
print(quentin_address) #This wil print none. get() returns None when the key is not found.

#Three other useful methods: Rather than blindly checking if a key exists, sometimes you want to see 
#ALL the keys that exist in a dictionary:
my_information.keys() #Check all the keys
#You can do the same thing to see all the value with ... values()
my_information.values()
#You can now know all the keys, all the values... but you don't know to which each correspond

#The values can be anything



#What is very common is to have dictionaries as values, to store more complex information.
my_friends_info = {
    'Nick':{
        'age': 41,
        "city": "Boulder",
        "hobbies": ["skiing", "cooking"]
    },
    "Sam": {
        "age": 35,
        "city":"Chiacgo",
        "hobbies":["hiking",'coffee'],
        "job": 'professor'
    } #Another key: Sam,one value: his dictionary of information
}

#How would we use a dictionary like this?

#How would you get your friend Nicks information?
my_friends_info["Nick"]
#We just got Nicks dictionary!
#Now, how would we get Nick's age from that dictionary?
my_friends_info["Nick"]["age"] #We index Nicks dictionary to get his age by using age index
#How would we get Sam's hobbies?>
my_friends_info["Sam"]['hobbies']
#What if you're not sure if you have information about a friend's job?
my_friends_info["Sam"].get('job') #if we do it for Sam, we get Professor
my_friends_info["Nick"].get('job') #if we do it for Nick we get nothing

#Mini assignment: Sam recently picked up birdingwatching. Can you add this hobby to his list of hobbies

my_friends_info['Sam']['hobbies'].append('birdwatching')
print(my_friends_info) #We can verify that we are getting sam's hobbies:

#This is a list. What do we know about lists?
#They are mutable: we can modify them in place. We can change their content, add to it
#or remove from it.
#If we grab this list, we can add to it using append()

my_friends_info['Sam']['hobbies'].append('birdwatching')
#It doesnt print anything, nothing gets returned
#If we check Sam'shobbies again:
my_friends_info["Sam"]['hobbies']

#ASIDE:
#Lets say we split this task into two:
# first we are recovering Sam's hobbies

#Lists are ORDERED collections of elements of any kind.
#WE can manipulate lists using INDEXING and SLICING to access and modify the elements that they contain
# WE can also use methods like .pop(), .append(), or insert() to do that. 

#Dictionaries are UNORDERED collections of key:value pairs
#We access the values by their key
#WE manipulate dictionaries using INDEXING to access and modify the values associated with given keys
my_friends_info[0] #returns an error, the key zero doesnt exist. Indexing by key and not position
