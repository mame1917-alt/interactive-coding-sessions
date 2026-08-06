import numpy as np
## Reminder, this is a one dimensional array:
one_d = np.array([1,2,3,4,5]) #Single argument, a list of numbers
# Remember: we can use the property .shape to see the shape of an array
print(one_d.shape)

# The innovation for this morning: WE are going to introduce 2-d arrays
# A 2-D array is like a matrix with rows and columns

#How do we create a 2-d array?
#Like this:
two_d = np.array( #Here is also a single argument
    [[1,2,3],
     [4,5,6]]
) #I have a list, that itself contains two lists. 
#Each of these inside lists correspond to a row of values in the matrix
print(two_d) # it shows a matrix with rows and columns 
# how many rows: the number of inside lists 
# how many columns: the number of elements in each list

print(two_d.shape)
# The first number is always the number of rows
# The second number is always the number of columns
# ORDER: (ROWS,COLUMNS)

#What happens if you index a 2-D array?
print(two_d[0]) #You are going to get the first row: [1,2,3]. This is an array
#A one dimensional array
print(two_d[1])

# So far, it's exactly like what we saw with lists and one-d array:
# When you index with a number you get the corresponding element
print(two_d[0:2]) # We get the first and second row. Our original 2-d array. 
#You can also slice a 2_D array, and it works in the same way

# So what's new then?
# Since 2_D arrays have two dimensions , we can use TWO sets of indices
# separated by a comma:
# The first one for the rows,the second one for the columns
print(two_d[0,0]) # We get 1: the element at the first two and first column
print(two_d[1,1]) # Element at the second row and second column is 5


#Lets practice a few more:
print(two_d[0,0:2])
print(two_d[1,1:2])
print(two_d[1:2,1:3]) #2-D array here again
print(two_d[-1,-1]) # Pay attention to what you are getting in the output
#If you use a slice, you keep that dimension
# If you use a index, you just get a single element

# INTRODUCTION OF NEW NOTATION
print(two_d[:,0]) #Just an empty colom ,called an 'empty slice'
#You get all the elements. All the rows, just column 0
#This is a one-d array.

two_d = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]) # This is a square matrix

print(two_d)

#Like on 1_D array, we can use slices and indexing to replace values
#. Exercise. Replace the value 5 by 999 using indexing

two_d[1,1] = 999
print(two_d) 
#Now make the final column be 7, 14, 21
two_d[:, 2] = [7, 14, 21]
print(two_d)
two_d[:, -1] = [7,14,21]
print(two_d) #prints same thing as above, just nit picky

#Again, same logic as on 1_d arrays.
#Let's restore our 2-D array

two_d = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]) 

#2-D arrays are ARRAYS.Meaning we can do the same thing
#we saw Tuesday on 1-D arrays

#Can you create an array that flags all the value in two_d
#that are greater than 5 (strictly greater)

mask = (two_d > 5)
print(mask)


    # Refresher on Boolean indexing: 
a = np.array([1,2,3,4,5])
b = np.array([False,True,True,False,True])
a[b] #We can apply the mask to the array and only get the values where the mask is true
# Another thing we saw is that we can use Boolean indexing to replace values:
a[b] = 999
print(a)

# The exact same logic applies to the 2-D arrays


two_d = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]) 

mask = (two_d > 5)
print(mask)

#Can we use this mask to replace all the values strictly greater than 5 with 999?
two_d[mask] = 999
print(two_d)

#Lets recreate our array one last time:
two_d = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]) 

mask = (two_d > 5)
print(mask)

print(two_d[mask])

b#We already saw that when arrays have compatible shapes, we can sum them:
print(a+b)
#Subtract them:
print(a- b)
#Multiply them:
print(a*b)
#Divide them:
print(a/b)
#You can add a single number to them:
print( a + 10)

#Finaal thing to learn:
#One Tuesday, we saw that arrays have methods:
one_d = np.array([1,2,3,4,5])
print(one_d.sum())
print(one_d.max())

#Two D arrays also have methods..with a very small twist
units_sold = np.array([
    [120,150,130,170],
    [75,60,90,80],
    [300,330,310,350]
]) #One thing to note: When creating an array, all the rows need to have the same 
# number of elements
print(units_sold) #Rows are products, columns are months (Jan-Apr)
#What happens if we do:
print(units_sold.sum()) #This is the GRAND sum. All the sum of all the products
# sold in all the months

#But what if we wanted instead to have the total per product?
#Or the total per month?
# This is where a nifty keyword comes in : axis = 
# This is an argument on most array methods
print(units_sold.sum(axis = 0))
# The axis tells us the dimension that we are collapsing
# That we are taking the method over
# Here we sum the dimension (0) (the rows) and are thus left with the columns
print(units_sold.sum(axis = 1)) # here, we do the opposite:
# We take the sum across the columns and are loeft with the rows

#Exercise 1: the method mean() gives you mean of an array
#It also takes an optional axis argument
# Use this method to give me the mean units sold in each of the four months

print(units_sold.mean(axis = 0))

# Exercise 2: Using the method max(), find the highest number of units sold across all products and months
print(units_sold.max()) #WE dont need axis because we want to find the highest value in all of the matrix

# Exercise 3: Find the minimum number of sales for product A across the 4 months
print(units_sold[0, :].min()) #Taking just the row for product a and taking the minimum on that
