# Define a simple function
def greet():
    """This function prints a greeting message."""
    print("Hello! Welcome to Python functions.")

# Call (execute) the function
greet()

def greet_user(name):
    """This function greets the user by name."""
    print(f"Hello, {name}! Nice to meet you.")

# Call the function with an argument
greet_user("Navitha")

def add_numbers(a, b):
    """Returns the sum of two numbers."""
    result = a + b
    return result  # Return the result to the caller

# Call the function and store the result
sum_result = add_numbers(5, 3)
print("The sum is:", sum_result)

def greet_person(name="Guest"):
    """Greets a person, default is 'Guest'."""
    print(f"Hello, {name}!")

# Calling without arguments uses the default
greet_person()

# Calling with a value overrides the default
greet_person("Navitha")

def calculate(a, b):
    """Returns sum, difference, and product of two numbers."""
    sum_val = a + b
    diff_val = a - b
    prod_val = a * b
    return sum_val, diff_val, prod_val  # Multiple return values

# Capture multiple outputs
s, d, p = calculate(10, 5)
print("Sum:", s)
print("Difference:", d)
print("Product:", p)
