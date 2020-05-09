#file io basic , control+slace is used for comment
"""
"r" - open file for reading - default mode
"w" - open file for write mode
"x" -creates file if not exist
"a" - add more content to a file
"t" - text mode - default mode
"b" - binary mode
"+" -read and write
"""
#Opening a file
f=open("manu.txt","rt") #here f is a file pointer ,it eturns by the open
print(f.readlines()) #read all line in a single line
#print(f.readline()) #read one line at a time
#print(f.readline())
"""read a function using file pointer"""
#content=f.read()
#print(content)

#for line in content: #it print character by character
 #   print(line)
for line in f: #read line by line
    print(line,end="")

"""
content=f.read(5) #we read the line using the word limit , here it takes file character and print after that in new line it print emaining character
print(content)
content=f.read(344) #here there is no that much character so it print its max character means all character
print("1",content)
content=f.read(3444)#here there is not that much caracter , so it is not printing anything
print("2",content)"""
#closing a file
f.close() #closing file is very neccessary bcoz when we open the file ,
# there is some resources who dealing with file ,and when we close the file means we release that resources


