# Set is an unordered collection of unique elements.
# basket = {"apple","orange","mango","apple","orange"}
# print(type(basket))
# print(basket)

# There is another method to initialize sets
# a=set()
# a.add(1)
# a.add(2)
# print(a)

# Set Curley brackets {} are never empty, if they are empty it will be considered as dictionary.
# a={}
# print(type(a))

# Set does not support index operation.

# Set allows to be used as constructor.
# numbers = [1,2,3,4,2,3,4]
# unique_numbers=set(numbers)
# print(unique_numbers)
# unique_numbers.add(5)
# print(unique_numbers)

# fs is frozen set, Frozen set doesn't allow to add new no to set.
# fs = frozenset(numbers)
# print(fs)
# print(fs.add(5))

# Another E.g for finding iteration in sets.
# x={"a","b","c"}
# print("a" in x )
# print("x" in x )
# for i in x:
#     print(i)


# Another E.g for finding union,intersection in sets.
# x={"a","b","c"}
# y={"a","g","h"}
# print(x)
# print(y)
# # For union use OR operation(|)
# print(x|y)
# # For intersection use AND operation(&)
# print(x&y)
# # Find difference between x and y
# print(x-y)
# # Find difference between y and x
# print(y-x)

# # for Finding sub-set
# print(x<y)
# # answer is false, since x is not a sub set of y.
# b={"h","g"}
# print(b<y)
# # Answer is true, since b is sub-set of y

