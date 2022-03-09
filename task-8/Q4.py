import numpy as np
import pandas as pd

l=[] # creating a empty list 
n = int(input("enter the number of elements in series: ")) 

# taking the elements in the list as input
for x in range(0,n,1):
    a=(input("enter the element: "))
    l.append(a)

# creating the series from list 
ser=pd.Series(l)
p= ser.size
print("")
for i in range(0,p,1):
    print(ser[i].title(), end=" ")

# the title function will capitalise the first letter of all the words within the element also
# whereas the capitalize function will only capitalize the first letter of the element , not all the words in element

""" if we want to take the default series then only the series will change and the code will look like 

ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
p= ser.size
for i in range(0,p,1):
    print(ser[i].capitalize(), end=" ")

"""


