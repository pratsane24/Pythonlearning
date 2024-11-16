# The loop control statement change the execution of the loop. When the execution leaves the scope,
# all automatic objects are get destroyed.

# different types of looping statement
# 1.Break statement
# Terminates the loop statement and transfer execution to the statement immediately following loop.
#  2.Continue Statement
# Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
# 3.Pass Statement
# The pass statement in python is used when a statement is required syntactically but you do not want any command or code to execute.

# 1.Break
# eg
# for letter in "Python":
#     if letter == "o":
#         # Here i am using break statement to break execution
#         break
#     print("Current Letter:",letter)
# print("Bye")


# Continue Statement
# eg
# for letter in "Python":
#     if letter == "h":
#         # Continue statement will skip the "h".
#         continue
#     print("Current Letter:",letter)
# print("Bye")
    
# Pass Statement
for letter in "Python":
    if letter == "h":
        pass
        print("Pass Block")
    print("Current Letter:",letter)
print("Bye")