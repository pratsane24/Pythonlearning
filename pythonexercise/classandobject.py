# Question:- Create a sample class named Employee with two attributes id & name?

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Creating an instance of the Employee class
emp1 = Employee(1, "John Doe")

# Accessing the attributes of the instance
print(emp1.id)
print(emp1.name)



# Question :- Use del property to first delete id attribute and then the entire object?
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def delete_id(self):
        del self.id

# # Creating an instance of the Employee class
emp1 = Employee(1, "John Doe")

# Deleting the 'id' attribute
emp1.delete_id()

# Accessing the 'name' attribute
print(emp1.name)

# Deleting the entire object
del emp1