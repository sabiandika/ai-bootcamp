# Example of Scope and Local Scope in Python

# Global variable (global scope)
x = 10


def example_function():
    # Local variable (local scope)
    y = 5
    print("Inside the function:")
    # Accessing global variable inside function
    print("x (global variable) =", x)
    # Accessing local variable inside function
    print("y (local variable) =", y)


example_function()

print("Outside the function:")
print("x (global variable) =", x)  # Accessing global variable outside function

# The following line would cause an error because y is local to the function
# print("y (local variable) =", y)  # Uncommenting this will raise NameError

"""
Explanation:
- Global scope: Variables defined outside any function or block, accessible anywhere in the code.
- Local scope: Variables defined inside a function, accessible only within that function.
- In this example, 'x' is a global variable accessible both inside and outside the function.
- 'y' is a local variable accessible only inside 'example_function'.
- Trying to access 'y' outside the function will result in an error.
"""
