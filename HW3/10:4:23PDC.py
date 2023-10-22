import numpy as np

list_2D = np.zeros((5, 5), dtype=int)
current_odd = 1
#Hint: Outer loop will manage row indices, inner loop will manage column indices (or vice 
# versa).
for i in range(5):
    for j in range(5):
        list_2D[i][j] = current_odd
        current_odd += 2

print(list_2D)

list_2D = list_2D.astype(object)  # Convert the data type to object to allow mixed types
for i in range(5):
    for j in range(5):
        if list_2D[i][j] % 3 == 0:
            list_2D[i][j] = '?'

print(list_2D)
