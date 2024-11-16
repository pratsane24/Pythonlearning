# What is JSON?
# JSON=Java Script Object Notation.
# JSON is a data exchange format similar to XML.
# JSON is a lightweight format compared to XML.

#JSON Format
# {
# "name":"tom",
#"address":"1 green street,NY", 
# "phone":"2323232323"
# } 
# 
# XML
# <name>tom</name>
#<address>1 green street,NY</address>
# <phone>2323232323</phone>

# Question:- We will write two programs,
# (i) To create address book & write some records into it.
# (ii)Read this address book.

book={ }
book['tom']={
'name': 'tom',
'address': '1 red street, NY',
'phone': 989898989
}


book['bob']={
'name': 'bob',
'address': '1 green street, NY',
'phone': 989898900
}

import json
s=json.dumps(book)
print(s)
with open("D://pythoncoding//book.txt","w") as f:f.write(s)

# Note :use pwd to get the correct path or location of your file.
# You can now read this JSON data using any language that supports JSON such as javascript,C++ etc.
# Hence this is called data exchange format(i.e. exchanging data from python program to javascript program).


# f=open("D://pythoncoding//book.txt","r") 
# s=f.read()
# print(s)

import json
book=json.loads(s)
# print(book)
# print(type(book))
# print(book['bob'])
print(book['bob']['phone'])

# for person in book:
#     print{book[person]}          