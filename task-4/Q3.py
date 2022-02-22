#declaring a list for storing student info and adding a list within it 
stuinfo=[["roll no.","name","marks"]]

#asking the user to enter the number of records
n=int(input("enter the no. of records "))

#loop to take the input from the user as rollno. name and marks then storing them in a seaparate list 
#appending the new list in the existing list stuinfo

for i in range (1,n+1):
    rollno=int(input("enter the roll no.: "))
    name=input("enter the name: ")
    marks= int(input("enter the marks: "))
    l1=[rollno,name,marks]
    stuinfo.append(l1)

print("\r")
#"\r" is used to get the print output after a line gap 

#loop will give the indivisual item as output 
for row in stuinfo:
    for item in row:
        print(item, end=" ")
    print(" ")

print("\r")

#the second row of the list stuinfo will be printed
print("the second row is: ")
print(stuinfo[2])
