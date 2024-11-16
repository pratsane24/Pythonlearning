# What is Conditional Statement?
# Condtional Statement in python perform different computations or actions depending on whether a specific Boolean constraint evaluates
# to true or false. Conditional statements are handled by IF statements in python.
# There are differnt types of conditions
# 1. If (It is simple if condition, there is only 1 condition).
# 2.If_Else
# 3.If_else ladder
# 4.Nested If


# 1.Simple IF
# var = 10
# if(var==10):
#     print("Value of variable is 10")
#     # your condition is getting true
# print("bye")

# # another e.g if not true.
# var = 15
# if(var==10):
#     print("Value of variable is 10")
# print("bye")

# # another e.g if not true.
# a=25
# if(a>=30):
#     print("Value of variable is",a)
# print ("bye")

# 2.If_else
# a=int(input("Enter the value of A: "))
# b=int(input("Enter the value of B: "))
# if a<b:
#     print("B is greater")
# else:
#     print("A is greater")

# another e.g
# x=25
# y=30
# if x<y:
#     print("Y is greater")
# else:
#     print("X is greater")

# 3.If Else Ladder
# Question:- i) Percentage greater than 70==Dist
            # ii) percentage greater or equal to 65 & less than 70==1st class
            # iii) percentage greater or equal to 60 & less than 65==2nd class
            # iv) percentage greater or equal to 55 & less than 60==3rd class
            # v) percentage less than 55==fail.

# Solution:-
# p = int(input("Enter your percentage: "))

# if p>70:
#     print("Dist")
# elif p>=65 and p<70:
#     print("1st Class")
# elif p>=60 and p<65:
#     print("2nd Class")
# elif p>=55 and p<60:
#     print("3rd Class")
# else:
#     print("Fail")
    # There is no need to but condition for fail, since every condition is mentioned in efil.Therefore the remaining condition is else. 


# 4.Nested IF
# Question:- Condition for blood donation
#              i)Age>=18
#             ii)Weight>=50
#             iii)If both age & weight match with creteria then the user can donate the blood.
#             iv)if age is less than 18 show msg underage
#             v)if weight is less than 50 show msg underweight.
#             vi)if age does not match then it should not ask for weight.
# Solution:-  
# age = int(input("Enter your age: "))

# if age>=18:
#     # In this you ask for weight input later since you have a condition if above 18 then only ask for weight.
#     weight = int(input("Enter your weight: "))
#     if weight>=50:
#         print("Donate blood")
#     else:
#         print("Underweight")
# else:
#     print("Underage")