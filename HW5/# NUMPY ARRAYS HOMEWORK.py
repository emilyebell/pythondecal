# NUMPY ARRAYS HOMEWORK

# DON'T USE FOR LOOPS!!!!!

"""
    if there is a problem with this line:
    do Command+shift+p or Ctrl+shift+p
    search Python: Select Interpreter
    select the 'base' or conda environment
"""
import numpy as np

# remember to run this line in the terminal to run doctests
# python3 -m doctest <file name>

# PROBLEM 1: HEY TWIN

"""
Given an array, find the rows where all the values are equal. 
"""
def findEqual(arr):
    """
    arr = np.array([[1, 1, 1], [1, 2, 3], [2, 2, 2]])
    >>> findEqual(arr)
    array([[1, 1, 1],
           [2, 2, 2]])
    """
    "YOUR CODE HERE"
def findEqual(arr):
    equal_rows = (arr == arr[:, [0]]).all(axis=1) # check individual colums along the rows for equivalency
    result = arr[equal_rows] # where are all values are equal
    return result
arr = np.array([[1, 1, 1], [1, 2, 3], [2, 2, 2]])
print(findEqual(arr))

# PROBLEM 2: CHECKERS

"""
Create an 8x8 array with a checkerboard pattern of 
zeros and ones using a slicing + striding approach
"""

def checkerboard():
    """
    >>> checkerboard()
    array([[1, 0, 1, 0, 1, 0, 1, 0],
           [0, 1, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0, 1, 0],
           [0, 1, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0, 1, 0],
           [0, 1, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0, 1, 0],
           [0, 1, 0, 1, 0, 1, 0, 1]])
    """
    "YOUR CODE HERE"
def checkerboard():
    board = np.zeros((8, 8), dtype=int) #0 matrix
    board[::2, 1::2] = 1 # even-indexed rows, odd-indexed columns = 1
    board[1::2, ::2] = 1 # odd-indexed rows, even-indexed columns = 1
    
    return board
print(checkerboard())


# PROBLEM 3: I NEED SOME SPACE

"""
Given an array of strings, return an array where
each letter in each string is separated by a space.
"""

def spaceBetween(stringArr):
    """
    >>> myarr = np.array(['python', 'is', 'cool!'])
    >>> spaceBetween(myarr)
    array(['p y t h o n', 'i s', 'c o o l !'], dtype='<U11')
    """
    "YOUR CODE HERE"
def spaceBetween(stringArr):
    spaced = np.char.join(" ", stringArr) #use char to add space
    return spaced
myarr = np.array(['python', 'is', 'cool!'])
print(spaceBetween(myarr))


# PROBLEM 4: EVERYTHING IS IN ORDER

"""
Given a multidimensional matrix, sort the matrix along the
columns.
"""

def sorting(bigMatrix):
    """
    >>> np.random.seed(12345)
    >>> a = np.random.randint(1,50, (4, 5))
    >>> a
    array([[35, 38, 30,  2, 37],
           [42, 38, 35, 30,  2],
           [15, 42, 28, 17, 10],
           [12, 14, 11, 18, 19]])

    >>> sorting(a)
    array([[12, 14, 11,  2,  2],
           [15, 38, 28, 17, 10],
           [35, 38, 30, 18, 19],
           [42, 42, 35, 30, 37]])
    """
    "YOUR CODE HERE"

def sorting(bigMatrix):
    return np.sort(bigMatrix, axis=0)

np.random.seed(12345)
a = np.random.randint(1, 50, (4, 5))
print("Original matrix:")
print(a)

sorted_matrix = sorting(a)
print("\nSorted matrix:")
print(sorted_matrix)