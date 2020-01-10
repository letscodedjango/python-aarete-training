# Here we will be discussing about the Python Datatypes

# Data types in python 
# int 
# float
# bool
# str

x = 56
y = 78.89

# print(type(x))
# print(type(y))

x = 568

def access_global_var():
    print(x)

def access_global_variable():
    print(x)


access_global_var()
access_global_variable()

class InstanceVar():
    def __init__(self):
        self.course = 'Python'
        self.title = 'Python Instance Variable'
        self.folks_count = 15

obj = InstanceVar()
print(obj.course)
print(obj.title)
print(obj.folks_count)


def local_variable():
    x = 67    # local variable
    y = 89    # local variable
    z = x + y
    print(z)