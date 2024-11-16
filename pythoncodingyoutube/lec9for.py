# Question:- Store monthly expenses in a list and find out total expenses for all months
# exp=[2340,2500,2100,3100,2980]
# total=exp[0]+exp[1]+exp[2]+exp[3]+exp[4]
# print(total)

# Note :- This can be done for short list what if you have 100 items?, so it will be very complicated to calculate that, 
# so to solve that we have for loop.


# exp=[2340,2500,2100,3100,2980]
# total=0
# for item in exp:
#     total=total + item
#     # print(total)
# print('total expense is:',total)

# Note:- in this I was facing a pbm with print option as the print (total) is in for loop so I was just getting
# the value for the total of expense in squence from 1 to end.
# but when print is out from the loop I m geting the sum of full range. 



# Question:- In our monthly expense example, print month no & expense & then in the end print total expense.
# exp=[2340,2500,2100,3100,2980]
# total=0
# for i in range(len(exp)):
#     print('month:',(i+1),'expense:',exp[i])
#     total=total+exp[i]
# print('total expense is:',total)


# Note:- in this for loops helps to help to add value one after the other,n keep the 1st value of total as 0 then the loop continuous till the end.



# Question :- Print no 1 to 10 using range()

# Note:- range() is a function in python, in which u have to put the starting value n 1+end value always.


# for i in range(1,11):
#     print(i)

# Note:- u can use any other variable name instead of i.


# Question :- Print quare of no 1 to 10 using range()
# for i in range(1,11):
#     print(i*i)


# Question:- Search for lost car key in home & when you found it stop searching.
# key_location="chair"
# locations=["living room","bed","kitchen","garage","chair","closet"]
# for i in locations:
#     if i==key_location:
#         print("key is found in",i)
#         break
#     else:
#         print("key is not found in",i)

# note:- key is found on chair so the loop is breaked at chair &  not went to closet. but it checked till the key was found.


# When u want to check for every no or items expect some the use the following method."Continue"
# Question:- Print square of no betn 1 to 5 expect even nos.
# for i in range(1,6):
#     if i%2==0:
#         continue
#     print(i*i)


# Note:- While Loop. While loops takes only 1 condition n until that condition is true it goes on in a loop.
i=1
while i<=5:
    print(i)
    i=i+1
    
    