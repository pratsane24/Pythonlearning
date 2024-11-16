# Google"python builtin exceptions" to see list of standard exceptions in python.
# We are using some standard exceptions we know in pririor.
# MemoryError is one of them.

# try:
#     raise MemoryError('memory error')
# except MemoryError as e:
#     print(e)

# How to define your own exceptions in python?
# We are now creating user defined exception.Exception is basically an instance/object of a class.
# User defined exceptions are always derived from Exception base class.

# class Accident(Exception):
#     def __init__(self,msg):
#         self.msg=msg
#     def print_exception(self):
#         print("User defined exception:", self.msg)

# try:
#     raise Accident ('crash between two cars')
# except Accident as e:
#     e.print_exception()


# example

# class Accident(Exception):
#     def __init__(self,msg):
#         self.msg=msg
#     def handle(self):
#         print("accident occured. take detour")

# try:
#     raise Accident ('crash between two cars')
# except Accident as e:
#     e.handle()


# Finally statement
# It is used to do clean up.
# If you are performing a program but it has got error in between so it stops their & doesn't reach towards the end of program.
# In long program for eg of 1000 lines it is difficult to get all the exceptions so finally keyword is used.
# It will always execute code in finally block no matter what!!
# E.g. 
# def process_file():
#     try:
#         f=open("D://pythoncoding//book.txt")
#         x=1/0
#     except FileNotFoundError as e:
#         print("inside except")
#     finally:
#         print("Cleaning up file")
#         f.close()
# process_file()