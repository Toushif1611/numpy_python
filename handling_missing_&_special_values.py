import numpy as np

'''
np.isnan(array) -> check for nan/missing values (nan = not a number)
np.nan_to_num(array, nan=value) default - 0 -> replace nan/missing with 0, inf/infinite with large finite number
np.isinf(array) -> check for inf/infinite values
'''

arr = np.array([1, 2, np.nan, 4, np.nan, np.inf, -np.inf])
print(np.isnan(arr))  # Check for NaN values
print(np.isinf(arr))  # Check for infinite values

print(np.nan == np.nan)  # NaN is not equal to NaN

cleaned_arr = np.nan_to_num(arr, nan=0.0, posinf=1000, neginf=-1000)
print(cleaned_arr)  # Replace NaN with 0 and inf with large finite numbers