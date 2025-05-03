# -------------------------------
# 1. String Data Type (Text Type)
# -------------------------------

# A string is a sequence of characters enclosed in quotes (single, double, or triple)
school_name = "XYZ Public School"
print(school_name)

# Use the type() function to check the data type of a variable
print(type(school_name))  # Output: <class 'str'>

# Strings are immutable — individual characters cannot be changed
# But you can assign a completely new string to the variable

# -------------------------------
# 2. Numeric Data Types
# Python has 3 numeric types: int, float, complex
# -------------------------------

# i. Integer (int)
# Stores whole numbers without decimals
school_phone_number = 12344323345682
print(type(school_phone_number), school_phone_number)
# Output: <class 'int'> 12344323345682

# ii. Float
# Stores decimal or fractional numbers
total_bill_amount = 837.46
print(type(total_bill_amount), total_bill_amount)
# Output: <class 'float'> 837.46

# iii. Complex
# Stores numbers with both real and imaginary parts (written as a + bj)
complex_number = 2 + 3j
print(type(complex_number))       # Output: <class 'complex'>
print(complex_number.real)        # Access real part → 2.0
print(complex_number.imag)        # Access imaginary part → 3.0

# -------------------------------
# 3. Sequence Types: list, tuple, range
# Sequences are ordered collections that support indexing
# -------------------------------

# i. List
# ✅ Ordered
# ✅ Mutable (you can change its contents)
# ✅ Allows duplicate values

fruit_list = ["apple", "banana", "orange", "cherry"]
print(type(fruit_list), fruit_list)  # Output: <class 'list'> [...]

# Modify an element (banana → tomato)
fruit_list[1] = "tomato"
print(fruit_list)  # Output: ['apple', 'tomato', 'orange', 'cherry']

# ii. Tuple
# ✅ Ordered
# ❌ Immutable (you cannot change its contents after creation)
# ✅ Allows duplicates

country_names = ("India", "Nepal", "USA", "United Kingdom")
print(type(country_names), country_names)  # Output: <class 'tuple'> [...]

# Uncommenting the line below will raise an error (tuples are immutable)
# country_names[2] = "Russia"  ❌ Not allowed

# iii. Range
# ✅ Ordered
# ❌ Immutable
# Used to generate sequences of numbers, especially useful in loops

# Syntax: range(start, stop, step)
# By default, step = +1

# Ascending range from 1 to 19 (stop is exclusive)
ascending_numbers = range(1, 20)
print(ascending_numbers)           # Output: range(1, 20)
print(list(ascending_numbers))     # Convert to list → [1, 2, ..., 19]

# Descending range from 100 to 51 (using step = -1)
descending_numbers = range(100, 50, -1)
print(list(descending_numbers))    # Output: [100, 99, ..., 51]

# Custom step: from 100 to 400, with step of 100
stepped_numbers = range(100, 500, 100)
print(list(stepped_numbers))       # Output: [100, 200, 300, 400]

# -------------------------------
# Quick Summary Table of Sequences
# -------------------------------
# | Type   | Mutable | Ordered | Allows Duplicates | Indexable |
# |--------|---------|---------|-------------------|-----------|
# | List   | ✅ Yes  | ✅ Yes  | ✅ Yes            | ✅ Yes    |
# | Tuple  | ❌ No   | ✅ Yes  | ✅ Yes            | ✅ Yes    |
# | Range  | ❌ No   | ✅ Yes  | ✅ Yes (default)  | ✅ Yes    |

