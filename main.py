# Function Definition Practice:
# Define functions according to the following prompts. Run the Replit to verify correct output.


# 1. Function that accepts no arguments. It's called say_hello and returns nothing, just prints 'hello'.
def say_hello():
  print("hello")

# 2. a 'sum' function that accepts two integers and returns the sum.
def sum(x,y):
  return x+y

# 3. an 'average' function that accepts two numbers and returns the average.
def average(x,y):
  return (x+y)/2

# 4. A function that accepts a first name and a last name and formats it to "{last_name}, {first_name}" (returns a string).
def format(first_name, last_name):
  return f"{last_name}, {first_name}"

# 5. A function that accepts a first name, last name, graduation year, and student number and returns those four items together in a list.
def grad_list(first, last, year, student_number):
  return [first, last, year, student_number]

# 6. A function that accepts an integer and returns whether it is above 18 or not (Boolean).
def over_18(x):
  return x > 18

#7. A function that accepts a string and prints the string in reverse (no return value).
def reverse(str):
  print(str[::-1])