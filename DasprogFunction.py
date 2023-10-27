#Nama : Fauzan Fuadiasnyah 
#NIM : J0403231085

#Call Function 
def fun():
    print("My fun function")
fun()

#Parameters & Arguments 
def sum(a,b):
    print(a+b)
sum(1,2)

#Arguments-Positional 
def greet(name, greeting):
    print(f"{greeting}, {name}!")
greet("Alice", "Hello")

#Arguments-keyword
def greet(name, greeting):
    print(f"{greeting}, {name}!")
greet(greeting="Hi", name="Bob")

#Arguments-default
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
greet("Eve") 

#Arguments - Arbitrary - *args
def print_args(*args):
    for arg in args:
    print(arg)
print_args(1, "apple", True)

#Arguments - Arbitrary - *kwargs
def print_kwargs(**kwargs):
 for key, value in kwargs.items():
    print(f"{key}: {value}")
print_kwargs(name="Alice", age=30)

#Arguments - Passing Lists/Dictionaries/etc.
def print_list(numbers):
 for num in numbers:
    print(num)

print_list([1, 2, 3, 4])

def print_dict(my_dict):
 for key, value in my_dict.items():
    print(f"{key}: {value}")

print_dict({"name": "Bob", "age": 25})

#Different argument combinations
def f(a, *b, c=6, **d): 
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}") 

f(1, 2, 3, x=4, y=5) 
f(1, 2, 3, c=7, x=4, y=5) 

#Return Statements-Examples
#This function adds two numbers and returns the result.
def add_numbers(a, b):
    result = a + b
    return result

sum_result = add_numbers(5, 3)
print(f"The sum is: {sum_result}")

#This function greets the person passed in as a parameter.
def greet(name):
     print(f"Hello, {name}!")
greet("Alice")

#executed at runtime
if 'a' == 'a':
    def greet():
        return "Hello, World!"
else:
    def greet():
        return "Hi there!"

def say_hello():
    print("Hello, World!")

greeting = say_hello # Assigning the function to a different name
greeting() # Calls the function
def say_hello():
    print("Hello, Python!")
say_hello() # Calls the updated function

#first class object
def greet(name):
    return f"Hello, {name}!"
my_function = greet
result = my_function("Alice")
print(result) 

#first class object - another examples
#Example 1
def apply(func, x):
    return func(x)
def square(x):
    return x * x
result = apply(square, 5)
print(result)
#Example 2
def get_multiplier(factor):
 def multiplier(x):
    return x * factor
 return multiplier
double = get_multiplier(2)
triple = get_multiplier(3)
print(double(5)) 
print(triple(5))

#Example
def my_function():
    x = 10 
    print(x)
def outer_function():
    y = 20 
    def inner_function():
        print(y) 
z = 30 
def another_function():
    print(z) 
print(len("Hello, World!"))

#Scope - Global keyword
global_var = 10 
def modify_global():
    global global_var 
    global_var = 20
modify_global()
print(global_var)

#Pass by Object Reference
def modify_list(my_list):
    my_list.append(4) # Modifying the list inside the function
my_list = [1, 2, 3]
modify_list(my_list)
print(my_list) # Output: [1, 2, 3, 4]

def reassign_list(list):
    list = [4, 5, 6] # Reassigning the list to a new object
list = [1, 2, 3]
reassign_list(list)
print(list) # Output: [1, 2, 3]

#Pass by Object Reference
def modify_integer(x):
     x += 1 # Modifying the integer inside the function
my_integer = 5
modify_integer(my_integer)
print(my_integer) # Output: 5

#Function Overloading
def product(a, b):
    print(a * b)
def product(a, b, c):
    print(a * b * c)
# product(4, 5) # Uncommenting this shows an error
product(4, 5, 5) # This line will call the last function
# Try using *args to solve that problem

#Function Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
result = factorial(5)
print(result) # Output: 120

#Error Handling - Example
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid data types")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    else:
        return result
    finally:
        print("Division operation complete")
# Example usages
print(divide(10, 2)) # Output: 5.0
print(divide(10, 0)) # Output: Error: Division by zero\nDivision operation complete\nNone
print(divide("10", 0)) # Output: Error: Invalid data types\nDivision operation complete\nNone

#Docstrings - Examples
#This function adds two numbers together.
def add(a, b):
    Args :
    a (int): The first number to be added.
    b (int): The second number to be added.
 
    Returns : 
    int: The sum of the two input numbers.
 
    Example :
    >>> add(3, 4)
    7
    return a + b
help(add) # Displays the docstring

