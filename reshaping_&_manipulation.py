import numpy as np

'''
#Reshaping

reshape(rows, column) specify new shape
if dimentions match

it does not create copy, it's just a view
'''
'''
arr = np.array([1,2,3,4,5,6])

reshape_arr = arr.reshape(3,2)
print(reshape_arr)
'''

'''
.ravel() -> view
.flatten() -> copy
'''
'''
arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d.ravel())
print(arr_2d.flatten())
'''