"""
HW 4: Debugging and Lists

Q1 Debugging

Throughout this homework, whenever you encounter an error, we would like you to 
explain in a comment what it was and how you fixed it. You can write all these errors 
at any place in the file.



Q2 List Slicing and Striding:

Part 1: Create a variable (name it anything you want but make it descriptive!) that 
is assigned to a list with the numbers 0 to 50. You should not have to write each 
number manually.
"""

# Q2 PART 1 CODE HERE 
import numpy as np

numbers_list = list(range(51))

"""
Part 2: Create a function that takes in a list and squares each element in the list.
"""

# Q2 PART 2 CODE HERE

def square_elements(numbers_list):
    input_array = np.array(numbers_list) #had to look up np.array couldn't even tell you what I was trying to do before
    squared_array = np.square(input_array)
    squared_list = squared_array.tolist()
    return squared_list
result = square_elements(numbers_list)
print(result)
""""""
input_list = [1, 2, 3, 4, 5]
result = square_elements(input_list)
print(result)  # Output: [1, 4, 9, 16, 25]

"""
Part 3: You are given two lists: listA and listB. listA contains the integers 1 through 
10 while listB contains the integers 20 through 30. Return a single, new list containing
only the odd integers of both lists in sorted order.
"""

listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listB = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# Q2 PART 3 CODE HERE
arrayA = np.array(listA) 
arrayB = np.array(listB)
odd_integers = np.concatenate([arrayA[arrayA % 2 == 1], arrayB[arrayB % 2 == 1]])
sorted_odd_integers = np.sort(odd_integers)

sorted_odd_integers_list = sorted_odd_integers.tolist()

print(sorted_odd_integers_list) #because my variable name was too large I was getting lots of errors associated with mistakes retyping it

"""
Q3 2D Lists
Using nested for loops, create and print a 5x5 2D list with the odd numbers from 1 to 25.
"""

# Q3 PART 1 CODE HERE
list_2D = np.zeros((5, 5), dtype=int)
current_odd = 1
#Hint: Outer loop will manage row indices, inner loop will manage column indices (or vice 
# versa).
for i in range(5):
    for j in range(5):
        list_2D[i][j] = current_odd
        current_odd += 2

print(list_2D)

# I was getting an error in this part because I had forgotten to define an object called "matrix" was in line 74, I fixed this by changing it back to list_2D

"""
Now with your completed list_2D, replace all multiples of 3 with '?' character and print
the resulting 2D list.
"""

# Q3 PART 2 CODE HERE
#What conditional can you use to check if numbers are multiples? --> list_2D % 3 == 0
list_2D = list_2D.astype(object) 
for i in range(5): #horiz.
    for j in range(5): #vert.
        if list_2D[i][j] % 3 == 0:
            list_2D[i][j] = '?'

print(list_2D)

"""
Q4 More List Practice

Write a function that takes in a list and returns a copy of that list with duplicate 
values removed.
"""

def remove_duplicates(input_list): # i always forget these stupid colons and get errors for it EVERYTIME
    input_array = np.array(input_list)
    unique_array = np.unique(input_array)
    unique_list = unique_array.tolist() #kept getting an error on this line, but I eventually had to look up more about the to list funtion
    return unique_list

input_list = [40, 10, 80, 50, 20, 60, 30]
result = remove_duplicates(input_list)
print(result)
