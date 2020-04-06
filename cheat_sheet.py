# commenting color legend
# ? Main Topic 
# * subtopic 

# ? Loops
# * if you have an array 
arr = [1,2,3]

# for num in arr:
#   print(num)

# * if you have a dictionary 
dict = {"c":"carlos"}

# for key in dict:
  # print(key) # * this will print each key in the dict dictionary

# * looping through an array not starting at 0
arr4 = [1, 2, 3]

# for num in range(1, len(arr4)):
#   print(num)

# ? Math
# * this will print out a float
#print(19/10)  
# * a couple of ways that you can turn a float into an into
# * if you have a postive number then you can do
int(19.45)
# * you could also do this 
import math 
math(19.45)



# ? Dictionaries

# * importing this to make a "Counter" instance of how many elelements there are in an array
from collections import Counter 

arr = [1,2,3,1,1]
dict = Counter(arr)
# * dict looks like this:
#{1:2,2:1,3:1}

# for key in dict:
#     print(key)


# print(1/10)

h ={}
# * putting an element into a dictionary
h["c"] = "yes"

# * checking if a key is within a dictionary 
# if "key" in h:
#   print("yes")



# ? Arrays 

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

# for num in range(1, len(arr4)):
#   print(num)




