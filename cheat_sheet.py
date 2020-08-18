# commenting color legend
# ? Main Topic 
# * subtopic 

# ? Truthy and Falsy values

# * Truthy
# non-empty sequences or collections (lists, tuplese, strings, dictionaries, sets)
# Numeric values that are not zero
# True

# * Falsy
# empty lists []
# empty tuples ()
# empty dictionaries {}
# empty sets set()
# Empty strings ""
# Empty ranges range(0)

# ? Random stuff
# * pass is a good placeholder for when python is expecting something 
pass


# ? Loops
# * if you have an array 
arr = [1,2,3]

# for num in arr:
#   print(num)

# * if you have a dictionary 
dict = {"c":"carlos"}

for key in dict:
  # print(key) # * this will print each key in the dict dictionary
  pass

# * looping through an array not starting at 0
arr4 = [1, 2, 3]

for num in range(1, len(arr4)):
#   print(num)
  pass

# ? Math
# * this will print out a float
#print(19/10)  
# * a couple of ways that you can turn a float into an into
# * if you have a postive number then you can do
int(19.45)
# * you could also do this 
import math 
# math(19.45)



# ? Dictionaries

# * importing this to make a "Counter" instance of how many elelements there are in an array
from collections import Counter 

arr = [1,2,3,1,1]
dict = Counter(arr)
# * dict looks like this:
#{1:2,2:1,3:1}

for key in dict:
    
    print(key)


# print(1/10)

h ={}
# * putting an element into a dictionary
h["c"] = "yes"

# * checking if a key is within a dictionary 
if "key" in h:
#   print("yes")
  pass

# ? Tuples ()
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

# ? Arrays 

# * popping out an element from an array
arr = [1,2,3]
arr.pop() # last element 
arr.pop(0) #first element 
arr.pop(n) # pop off nth element

# * appending items to an array
arr = [1,2,3]
arr.append(4)

# print(arr)

# * getting length of an array
arr1 = [1,2,3]
len(arr1)

# * slicing through an array

arr2 = [1,2,3,4]
start = 1
stop = 2

arr2[start:stop]  # items start through stop-1
arr2[start:]      # items start through the rest of the array
arr2[:stop]       # items from the beginning through stop-1
arr2[:]           # a copy of the whole array

# * getting last item in an array 
arr3 = [1,2,3]
arr3[-1]

# * looping through an array not starting at 0 
arr4 = [1,2,3]

for num in range(1, len(arr4)):
#   print(num)
  pass

# * turn an array of strings into a string
arr = ["c","a","r"]

# print("".join(arr))

# * sorting an array 
arr = [2,1,3]

# print(sorted(arr))

# * reduce function
def add(acc,el):
  acc + el

arr = [1,2,3]
# reduce(add,arr)

# * reveersing an array
arr = [1,2,3]
reversed(arr) # this does not return a list however

#you can return a list by doing this:
reversed_arr = list(reversed(arr))

# ? String

# * sorting a string 
str = "carlos"
# print(sorted(str)) # sorting a string will return an array

# * turning string into array
str1 = "carlos"
list(str1) # will turn str1 intto an array

# ? Classes
# * example 


class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  items_in_cart = {}

  def __init__(self, customer_name):
    self.customer_name = customer_name

  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print(product + " added.")
    else:
      print(product + " is already in the cart.")

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print(product + " removed.")
    else:
      print(product + " is not in the cart.")


my_cart = ShoppingCart("carlos")
my_cart.add_item("banana", 2.50)
