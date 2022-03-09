import numpy as np

print("enter the number of rows")
row = int(input())
print("enter the number of columns")
column = int(input())

main_list1 = []

print("enter the elements for first array: ")
for i in range(row):
    list1 = []
    for j in range(column):
        z = int(input())
        list1.append(z)
    main_list1.append(list1)

main_list2 = []

print("enter the elements for second array: ")
for k in range(row):
    list2 = []
    for l in range(column):
        y = int(input())
        list2.append(y)
    main_list2.append(list2)

arr1 = np.array(main_list1)
arr2 = np.array(main_list2)

print("the first array is")
print(arr1)
print("the second array is ")
print(arr2)

arr3 = np.add(arr1,arr2)
print("the sum of arrays is: ")
print(arr3)
