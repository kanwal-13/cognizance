import numpy as np

print("1st")
print(0 * np.nan)
# this returns nan because it nan stands for not a number that is null and if there is no number then even after multiplying with 0 it will be nan

print("2nd")
print(np.nan != np.nan)
# the content of NaN is never equal to the content of another NaN because they have a different id

print("3rd")
print(np.inf > np.nan)

print("4th")
print(np.nan - np.nan)
# this returns nan because it nan stands for not a number that is null and if there is no number then even after subtracting it will be nan

print("5th")
print(0.3==3 * 0.1) 
# this returns false because computer carries the operation in binary format and not in decimals. so there is a difference of precision.