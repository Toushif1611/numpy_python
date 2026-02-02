import numpy as np

'''
np.insert(array, index, value, axis= none)
array - original array
index - 
value - 
axis - 
axis = 0, row-wise
1, column-wise
'''
'''
arr = np.array([10,20,30,40,50,60])
print(arr)
new_arr = np.insert(arr, 3, 60, axis=None)
print(new_arr)
'''
'''
arr_2d = np.array([[1,2,1],[4,5,1]])

print(arr_2d)
new_arr_2d = np.insert(arr_2d, 2, [5,6,7], axis=0)
print(new_arr_2d)
'''
'''
arr = np.array([[10,20,30],[40,50,60]])
new_arr = np.append(arr, [[70,80,90]], axis=0)
print(new_arr)
'''

'''
np.conccentrate((arr1, arr2), axix=0)

axis 0 -> vertical stacking
axis 1 -> horizontal stacking
'''
'''
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

new_arr = np.concatenate((arr1, arr2))
print(new_arr)
'''
'''
np.delete(array, index, axis = none)
flattern array
'''
'''
arr = np.array([[10,20,30],[40,50,60]])
print(arr)
new_arr = np.delete(arr, 0, axis=0)
print(new_arr)

'''
'''
stacking arrays
vertically
horizontally

vstack((arr1, arr2)) row wise
hstack((arr1, arr2)) column wise
'''
'''
arr = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(np.vstack((arr, arr2))) # vertical stacking
print(np.hstack((arr, arr2))) # horizontal stacking
'''
'''
np.split(array, number of splits, axis= none)
np.vsplit(array, number of splits)
np.hsplit(array, number of splits)
'''
arr = np.array([10,20,30,40,50,60,70,80])
print(arr)
print(np.split(arr, 4))


