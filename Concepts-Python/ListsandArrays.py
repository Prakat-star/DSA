# lists are the built in data structue that serves as dynamic array..
# lits are ordered, mutable , and can contain elements of different types..

# Empty list
x = []

# List with values
y = [1,2,3,4]

# List with mixed types
z = [0,"meow",3.14159,True]

# List comes with serevral build-in algorithms called methods, such as .append() , .sort() , and more.
x.append(2)
x.append(3)
x.append(1)
# here we append an empty list
x.sort()
# and sorted

# when we want to perform actions that are not built into python then we can create our own algorithms
# creating an algorithm to find the lowest value in a lsit..

my_array = [7, 12, 9, 4, 3, 11, 8]
minVal = my_array[0]
for i in my_array:
    if i<minVal:
        minVal = i
print("Lowest Value: ", minVal)

# This algorithm is very simple and fast for small data sets but if the data is big any algorithm will talk time this is where OptimiZaion comes in..
# Time Complexity:
# the time the algorithm needs to run is proportional, or linear, to the size of the data set. 
 