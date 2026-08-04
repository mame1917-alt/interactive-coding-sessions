
#imports are always at the top of your file:
import numpy as np #import x as y. x is the library name, y is the shorthand
#When libraries have short names, like math, we dont use a shorthand
import math
import pandas as pd
#The first thing we are going to do is soemthing we've done before:
# import a library
#If a library is not installed, what do we do?  UV
#in a regular terminal, type: UV add pandas numpy

#Once you've installed and imported a library., you can access its content using the dot notation:
print(math.pi)
print(math.sqrt(9))

#Lets talk about arrays now. Arrays are a new kind of object that live inside the numpy package
my_array = np.array([1,2,3,4,5,]) #You create an array by supplying a list of elements
print(my_array)
#it looks a lot like a list
#You can index it:
print(my_array[1])
#You can slice it:
print(my_array[0:3])
# So what's the difference really?
type(my_array)
# First difference: an array requires that ALL its elements are of the same type
my_list = ["Quentin", False, 42]
print(type(my_list[0])) #Str
print(type(my_list[1])) # Bool
#What if I create an array from this?
my_array = np.array(my_list)
print(my_array) #All elements have been converted to string
#In technical term, we say they were coerced to a common type
#They all convert to a string because it is the easiest to change all the types too
#It finds a common type for all the elements to be converted to

#Because all elements of arrays have the same type,
# arrays itself have what is called a dtype, short for data type:
print(my_array.dtype)
#Other examples
float_array = np.array([3.14,2.16,1.5])
print(float_array.dtype)

int_array = np.array([3,4,5])
print(int_array.dtype)

#Second distinction between lists:
# Arrays have FIXED SIZE
# You cannot add or remove elements from an array after it was created
my_list=[1,2,3,4,5]
my_list.pop()
print(my_list) #The po method has removed the last element of the list
my_list.append(6)
print(my_list) #The append method has added an element to the list

#What about arrays now?
my_array = np.array([1,2,3,4,5]) #I create it here
my_array.pop()
my_array.append()
my_array.insert()
#all the methods that exist on strings that allow you to add or remove elements 
# in a string do not exist for arrays

#Instead you need to use functions to create new arrays:
my_bigger_array = np.append(my_array,6) #This will creeate a new array that has the same content
#as my_array, plus the element 6 appended to the end
print(my_array)
print(my_bigger_array)

#Summary: Arrays are more constrained.They have the same data type.
#They have fixed length

#These restrictions enable very powerful things:

#Let me show you:
# First, lets not use arrays.
prices = [9.99,19.99,4.99,14.99,24.99]
quantities = [120, 75, 300, 50, 40]
#Say I want to calculate, for each product, the total revenue : price * quantity
#for each of these five products
#How would I do that?
totals = []
for (p ,q) in zip(prices,quantities):
    t = p * q
    totals.append(t)
    print(totals) # You cant really see it, but this operation is sloooowwwww

#What arrays allow you is to do vectorized operations. Rather than taking the elements one by one, 
# and checking one by one if the operation is allowed and how it works,
# Arrays are going to perform all the calculations at once on all the elements

arr_prices = np.array(prices)
arr_quantities = np.array(quantities)
print(arr_totals)  #I can just multiply the arrays directly

# Other examples:
# WE can compare them
totals = units_jan + units_feb
print(totals)
#How much more or less we sold in feb compared to jan?
print(units_feb - units_jan)
#Growth rate over the two months?
print(units_feb / units_jan)

#A restriction though
units_jan = np.array([120,75,300,50,40])
units_feb = np.array([150,60,330,80])  #Only data for four products
#The number of elements in an array is called the SHAPE:
print(units_feb - units_jan) #The two arrays do not have the same SHAPE
#The number of elements in an array is called the SHAPE:
print(units_jan.shape)
print(units_feb.shape) #To sum,divide, or multiple two arrays, they need to have compatible shapes
#By the way, this is why we cannot add or remove elements from arrays: we need to now their shape
#at all times

# We can compare them
units_jan = np.array([120,75,300,50,40])
units_feb = np.array([150,60,330,80,25]) #Units sold for five different products, in Jan and Feb

feb_sold_more = units_feb > units_jan
print(feb_sold_more)

#You can square an array
print(units_jan ** 2) #again applies the operation in a vectorized way, to each of the elements

#You can also use the square root ( if we are careful to use the numpy version)
print(np.sqrt(units_jan)) #the umpy library contains special versions of common math operations
#that are specifically designed to work with arrays

# error: We recorded 10 fake transactions for each of the products in Jan:
print(units_jan - 10)

# There are many operations you can apply to arrays... and arrays also have methods

units_jan.mean() #you can call the method mean() to know the mean value of an array...if the array
#has a numeric dtype

units_jan.max()
units_jan.std()


#WE have seen that we can index and slice arrays like lists:
prices = np.array([10,5,30,8])
print(prices[0]) #The first price
print(prices[0:3]) # The first three prices
#When you INDEX with a single value, you get the value of the dtype of the array
#When you SLICE an array, you get a new array

# When working with arrays, like with lists, you can edit the elements of the array
# lets replace the first price by 15:
prices[0] = 15 
print(prices)
#What if we want to now make the first two pricfes equal to 15 and 7?
prices[0:2] = [15,7]
print(prices)
#Arrays are still mutable! We just cannot change their shape

#Everything that we've seen so far with indexing and slicing
#is identical to what we could do with lists

#We can do more powerful stuff with arrays

# 1)  'MASKING' OR 'BOOLEAN INDEXING'
# We can index an array with a Boolean array of the same shape
my_mask = np.array([True,False,True,False,True]) #This is a mask
prices = np.array([15,7,20,30,8])
# I have my array and my mask
print(prices[my_mask]) # I can index the prices using the mask, put the mask between square brackets
#after the array, everywherre that its true we get the value. Everything that is not true is not
#When you index with a mask, you are going to get in return only the values of the array
#Thnk of overlaying the mask on top of the array: the true are the cutouts. ANy value that is 
#in the cutout is going to be returned

# When are masks useful?
quantities = np.array([5,10,15,-5,-7,10]) #quantities cannot be negative, so this array contains 
#some coding errors
#Could we create a mask that woudl reveal these errors?
my_mask = quantities < 0  #We get a mask: An array of shape 6, that contains True or False elements
print(my_mask) #Now we have the mask
#How can we use it to spot all the erroneous values in quantities?
print(quantities[my_mask]) # We us the mask to see all the negative values in quantities and get them 
#in an array
#Now, can we use the mask to replace all these negative values by 0?
quantities[my_mask] = 0 #You use the mask to highlight all the negative values and you assign the value
# zero to them
print(quantities)

quantities = np.arrays([5,10,15,0,0,10]) #This is the number of customers a coffee shop had 
#Monday through Saturday
# 1). On average, how many customers did they see on these six days? (reminder: .mean() is a method
# that gives you the mean of an array)
# 2.) On all the days they saw at least one customer, how many customers did they see on average?

#1)
print(quantities.mean())

#A2
my_mask = (quantities >= 1)
print(my_mask)
#WE can now apply the mask
non_zero_days = quantities[my_mask]
print(non_zero_days)
#What is the final step?
print(non_zero_days.mean())

#Note that we could have done it in this one line:
quantities[quantities >= 1].mean() #What is between square brackets is the mask:
#We dont need to store it into a variable first

#Final thing with arrays : FANCY INDEXING 
#Lets say you have emails from four customers:
emails = np.array(["mame1917@colorado.edu", "gal@yale.edu","puntoni@wharton.edu","gino@nbs.com"])
#How do wwe get the first email of the list?
print(emails[0])
print(emails[0:2])
#With lists you can only (i) index with a single value OR (ii) use a slice
#With arrays, you can index with multiple values
print(emails[[0,0,1,2,0]]) #You give a LIST of values as an index
#note the double bracket, first set to index, second set to define the list.
# if it makes it easier to process, you can break it down in two lines
my_indices = [0,0,1,2,0]
print(emails[my_indices])

#Why fancy indices? Very common: select a random sample of rows in a dataset

# lets wrap up on arrays:

    # 1) An Array is a new type of iterable. It works a lot like a list
    # 2) Exception 1: arrays only contain values of the same type. The data type of an array is called its dtype.
    # 3) Exception 2: arrays have a fixed shape. They can't be pop(),append() or insert()
    # 4)  Thanks to these restrictions, arrays can be added to each other, subtracted from each other, 
    #its elements can be multiplied, squared, divided, exponerated..whatever you want. These operations
    # are performed on all elements of the array and are much faster
    # 5) Arrays can be compared, element-wise, to create Boolean arrays (also called masks)
    # 6) You can use these masks to filter arrays and re-assign values at specific positions.
    # 7) Arryas, like lists, can be indexed and sliced, both to select and replace values
    # 8) Compared to lists, arrays except two new forms of indexing: Boolean indexing ( only the values
    #facing the True values in the mask are returned), and Fancy Indexing (all the indeices specified
    #in the list are returned)