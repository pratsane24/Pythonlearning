# Question :- Write a program that asks a user to enter a no. Program should tell if no. is odd or even.

# num=input("enter a number: ")
# num=int(num)
# # Note:-here num is string so we want to convert it into integer therefore are using int() here.
# if num%2==0:
#     print("number is even")
# else:
#     print("number is odd")



# Question:- Write a program that asks user to enter dish name and it should print which cuisine is that dish

indian=["samosa","dal","naan"]
chinese=["egg roll","pot sticker","fried rice"]
italian=["pizza","pasta","risotto"]

dish=input("enter a dish name: ")

if dish in indian:
    print(indian)
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("based on little knowledge i don't know which cuisine it belongs to",dish)


# Note:- elif is used if you have multiple options to be checked in if else.

# Note:- VArious operators in ptyhon
# 4==4 :- equal to 
# 4!=5 :- Not equal To 
# 2>1 :- 2 is greater than 1.
# 2<3 :- 2 is less than 3
# 2>=2 :- 2 is greater than or equal To 2.
# 3<=4 :- 3 is less than or equal to 4.
# 3>2 and 4>1 :- AND function :;- if the condition is statisfied for both condition than the value will be true. if anyone of the 2 condition is not statisied than the value will be false.
# 3>2 or 4>5 :- OR function :- atleast one condition from 2 is statisifed than the value is true.
# not 4==4 :- not true :- not true means false.

