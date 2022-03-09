import numpy as np

print("enter the number of rows for first matrix ")
row1 = int(input())
print("enter the number of columns for first matrix ")
column1 = int(input())

print("enter the number of rows for second matrix ")
row2 = int(input())
print("enter the number of columns for second matrix ")
column2 = int(input())

if (column1==row2):
    main_list1 = []

    print("enter the elements for first matrix")
    for i in range(row1):
        list1 = []
        for j in range(column1):
            z = int(input())
            list1.append(z)
        main_list1.append(list1)

    main_list2 = []

    print("enter the elements for second matrix")
    for k in range(row2):
        list2 = []
        for l in range(column2):
            y = int(input())
            list2.append(y)
        main_list2.append(list2)

    arr1 = np.array(main_list1)
    arr2 = np.array(main_list2)

    print("")
    print("the first matrix is")
    print(arr1)
    print("the second matrix is ")
    print(arr2)
    print("")

    print("the product of matrices is")
    arr3 = np.dot(arr1,arr2)
    print(arr3)

else:
    print("")
    print("the matrix multiplication is not possible as the number of column in first matrix are not equal to number of row in second matric which is a necessary condition for matrux multiplication")
    print("")