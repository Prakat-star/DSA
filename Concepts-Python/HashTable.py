# Hash Table : a Hash Table is a data structure designed to be fast to work with.
# it is prefered because searching , adding and deleating data can be done really quicky even for large amount of data in comparasion to arrays or linked lists.
# Hash Function is used to go directly to where data is stored making it really fast..

"""
Building a hash table:

1. Create an empty list. (can also be dictionary or set but i mean everyone like list right?)
2. Create a hash function..
3. Inserting an element using a hash function.
4. looking up an element using a hash function.
5. handling collisions.

"""

# Steap 1 : Create an empty list.
my_list = [None, None, None, None, None, None, None, None, None, None]
# or instead of typing all that shi. we can do the thing below works same and less effort... 
my_list = [None] * 10
# Each of these elements is called a bucket in a Hash Table.

# Step 2 : Create a Hash Function.
"""
sooo, the important part, we want to store data into it;s right place in the list
this is where hash function comes in..
hash function can be made in many ways, it is upto us how we wanna make it.
a common wat is to find a way to convert the value into a number that equals one of the hash table;s index

here i will create a hash function that sums the unicode numbers of each character and 
return a number between 0 and 9 . cus (my_list = [None] * 10) we have 10 operations with index from 0-9.
"""

def hash_func(value):
    sum_of_char = 0
    for char in value:
        sum_of_char += ord(char) # ord() give ascii value
    return sum_of_char%10

# this creates an hash func for each data... now we insert it to the hash table

# Step 3 :Inserting an element using a hash function.
def add(data):
    index = hash_func(data)
    my_list[index] = data

add('this')
add('way')
add('you')
add('can')
add('add')
add('whatever')
add('you')
add('want')
add('in the')
add('table')
print(my_list)
# you should have found out the shit thing about this method but still let;s search for some data. we will solve this problem in step 5.

# step 4 : looking up an element using a hash function.
def contains(data):
    index = hash_func(data)
    return my_list[index] == data
print(contains('table'))

"""
step 5 : handling collisions.

in the data we added above the data 'this' and 'table' gets same index so their ascii value must have 0 as thr last digit 
since 'table' get assigned 0 index last, it replaces 'this' in the table
This is called "COLLISION"..
to fix collision we can make room for more elements in the same BUCKET. solving the collision this way
is called "CHAINING" means giving room for more elements in the same bucket.

"""

"""

# For chaining we need lists within list. that can be accesed using index...
why my_list = [[]] * 10 doesnot work it makes lists within list but when we try my_list[0] = 'something'. that something will be 
saved not only to the index 0 list but to all the lists within the list . that is not something we want. so we can use
my_list = [[] for _ in range(10)] to perform same thingy as my_list = [None] * 10...

"""

my_list = [[] for _ in range(10)]
def add(name):
  index = hash_func(name)
  my_list[index].append(name)

add('this')
add('way')
add('you')
add('can')
add('add')
add('whatever')
add('you')
add('want')
add('in the')
add('table')
print(my_list)

# this way we can store multiple datas in a single bucket.
# but this way the search will take little bit longer time/ but still fasterrrr than searching the entire table..right

"""
uses:
1. Checking if something is in a collection
2. Storing unique items and quickly finding them
3. Connecting values to keys

""" 

# Time Complexity : O(1) on average.

"""
Hash Table elements are stored in storage containers called buckets.
    -A hash function takes the key of an element to generate a hash code.
    -The hash code says what bucket the element belongs to, so now we can go directly to that Hash Table element: to modify it,
        or to delete it, or just to check if it exists.
    -A collision happens when two Hash Table elements have the same hash code, because that means they belong to the same bucket.
    -Collision can be solved by Chaining by using lists to allow more than one element in the same bucket.
"""