# What is file handling?
# File Handling is an important part for web application.
# When can do serval functions for creating,Reading,Updating, and Deleting files.

# File handling Permissions
# "r" :- Read a file content
# "a" :- Append a value in file
# "w" :- Write a value in file

# What we can do?
# Create a file
# Read a file
# Append a file
# Storing list into file
# Read list from file

# # File creating
# # open method ("File name","Permission")
# Write method
# s="This is my file handling program"
# file = open("demo1.txt","w")
# file.write(s)
# print("File created")
# file.close

# # File Method
# # Whenever u are giving read permission, u should always have that file, other error will occur file not found.
# file = open("demo1.txt","r")
# filecontent=file.read()
# print(filecontent)

# # If we want to store any list in the file?
# l1 = ["python","php","java","angular"]
# # In this, list will be stored as single string,Single block memory.
# file = open("demo2.txt","w")
# file.writelines(l1)
# print("File Created")
# file.close()

# # Read a list from file
# file = open("demo2.txt","r")
# filelist = file.readlines()
# print(filelist)

# # Appending the value into file
# # Appends always add values in the end of the existing file.
# s="Python file handling"
# file = open("demo1.txt","a")
# file.write(s)
# print("File updated")
# file.close()

# E.g real world eg like our whatsapp.
# Zoom,Microsoft team.
# In all this eg we get a option of attaching a document.

