# a=["hey","bro","you'r","awesome"]
# for i in a:
#     print(i)


# # print(dir(a))
# itr=iter(a)
# print(itr)

# OUTPUT:- OF dir(a)
# This are built-in method.
# ['__add__', '__class__', '__class_getitem__', '__contains__',
#  '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
#   '__format__', '__ge__', '__getattribute__', '__getitem__',
#    '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
#     '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
#     '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
#     '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', 
#     '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index',
#      'insert', 'pop', 'remove', 'reverse', 'sort']


# print(next(itr))
# # # NOTE:-Use alt+P for repeating the last command in IDLE.
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(dir(itr))
# OUTPUT:- FOR dir(itr)
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#  '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
#  '__le__', '__length_hint__', '__lt__', '__ne__', '__new__',
#  '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
#  '__setstate__', '__sizeof__', '__str__', '__subclasshook__']


# itr=reversed(a)
# # It is use to reverse the iteration list.
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# Question:-
# Implement Remote Control Class that allows you to press "next" button to go to next TV channel?
class remotecontrol():
    def __init__(self):
        self.channels = ["HBO","cnn","abc","espn"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index +=1
        if self.index == len(self.channels):
            raise StopIteration

        return self.channels[self.index]

r=remotecontrol()
itr=iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

# If you print extra ,print(next(itr)) then u will get the following output.
# HBO
# nn
# abc
# espn
# Traceback (most recent call last):
#   File "d:\PYTHON\pythoncoding\lec20iterators.py", line 68, in <module>
#     print(next(itr))
#   File "d:\PYTHON\pythoncoding\lec20iterators.py", line 58, in __next__
#     raise StopIteration
# StopIteration
