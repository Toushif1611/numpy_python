import numpy as np
'''
prices = np.array([100, 200, 300, 400, 500])
discount = 10

final_prices = prices - (prices * discount/100)
print(final_prices)
'''

'''
meltching dimensions -> [1,2,3] + [10,20,30] ==> [11,22,33]
expanding dimensions -> [1,2,3] + [10] ==> [10,20,30]
incompatible dimensions -> [1,2,3] + [10,20] ==> error
'''
'''
arr_1d = np.array([1,2,3])
result = arr_1d * 10
print(result)
'''
matrix = np.array([[1,2,3],[4,5,6]]) #2x3 matrix
vector = np.array([10,20,30]) #id array with 3 elements
result_2d = matrix + vector
print(result_2d)
