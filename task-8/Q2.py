import numpy as np
from pandas import array

# Two arrays are said to be equal if both of them contain the same set of elements
# arrangements (or permutation) of elements may be different though.

# creating empty list 
l1=[]
l2=[]
n = int(input("enter the number of elements in array "))

print("enter the elements of first array ")

for x in range(0,n,1):
    a=int(input("enter the element "))
    l1.append(a)

print("enter the elements of second array ")

for y in range(0,n,1):
    b=int(input("enter the element "))
    l2.append(b)

print("")

# creating array from the list 
arr1=np.array(l1)
arr2=np.array(l2)

print("first array: ")
print(arr1)

print("second array: ")
print(arr2)

# sorting the array
arr1=np.sort(arr1)
arr2=np.sort(arr2)

w=True

# checking if the arrays are equal
for p in range(0,n,1):
    if(arr1[p]!=arr2[p]):
        w=False
        break

print("")
print(w)
print("")

# the random.randint function can also be used to get a system generated random array instead of user input

"""
instead of loop these pre defined functions can also be used

x = np.allclose(arr1, arr2)
print(x)

y = np.array_equal(arr1,arr2)
print(y)

the all close function is used for floating point numbers
Floating point calculations have inherent precision loss, so there are numbers which should be equal but differ by a very tiny amount.
array_equal is designed to be used with arrays of integers and only checks for exact equality.

"""