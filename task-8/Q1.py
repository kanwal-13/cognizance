import numpy as np 

firstno = int(input("enter the initial number: "))
lastno = int(input("enter the last number: "))
# creating an empty list
l = []

# creating the vector
for x in range(firstno,lastno,1):
    l.append(x)
    
    for i in range(5):
        l.append(0)

l.append(lastno)

print(l)