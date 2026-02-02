'''
#Indexing

array[index] #1d array
array[row, column] #2d array
'''
import numpy as np

'''
arr = np.array([10,20,30,40,50])

print(arr[0]) #first element
print(arr[2])
print(arr[-1]) # last element
'''

'''
# Sclicing

arr[start:end] , start to end - 1

negative step, -1 reverse
'''
'''
arr = np.array([10,20,30,40,50])
print(arr[1:5]) #index 1 to 4
print(arr[:4]) #index 0 to 3 
print(arr[::2]) #every second element
print(arr[::-1]) #element reverses
'''
'''
#Fancy indexing

arr = np.array([10,20,30,40,50])

print(arr[[0, 1, -1]])
'''
'''
#filtering

arr = np.array([10,20,30,40,50,60])
print(arr[arr>29])
'''

