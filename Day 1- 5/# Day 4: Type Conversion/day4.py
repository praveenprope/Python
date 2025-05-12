# 🧠 Type Conversion in Python

# Type conversion means converting one data type to another.

# Two types of type conversion:
# 1. Implicit Type Conversion (Automatic)
# 2. Explicit Type Conversion (Manual / Type Casting)

# ---------------------------------------------
# 🔹 1. Implicit Type Conversion (Automatic)
# Python automatically converts data types when needed.

x = 10        # int
y = 5.5       # float
c = x + y     # int + float = float
print(c)           # Output: 15.5
print(type(c))     # Output: <class 'float'>

# ---------------------------------------------
# 🔹 2. Explicit Type Conversion (Type Casting)

# Manual conversion using functions:
# int(), float(), str(), bool(), list(), tuple(), set()

# ---------------------------------------------
# 🔸 i. int() – Convert to Integer

# From String to Integer
stringInteger = "20"
print(type(stringInteger), stringInteger)             # <class 'str'> 20
convertToInteger = int(stringInteger)
print(type(convertToInteger), convertToInteger)       # <class 'int'> 20

# From Float to Integer
floatNum = 5.9
intNum = int(floatNum)
print(type(intNum), intNum)                           # <class 'int'> 5

# ---------------------------------------------
# 🔸 ii. float() – Convert to Float

# From String to Float
stringFloat = "20.70"
convertToFloat = float(stringFloat)
print(type(convertToFloat), convertToFloat)           # <class 'float'> 20.7

# From Integer to Float
intValue = 15
floatValue = float(intValue)
print(type(floatValue), floatValue)                   # <class 'float'> 15.0

# ---------------------------------------------
# 🔸 iii. str() – Convert to String

num = 100
convertToStr = str(num)
print(type(convertToStr), convertToStr)               # <class 'str'> "100"

# ---------------------------------------------
# 🔸 iv. bool() – Convert to Boolean

print(bool(0))             # False
print(bool(1))             # True
print(bool(""))            # False
print(bool("hello"))       # True
print(bool([]))            # False
print(bool([1, 2, 3]))     # True

# ---------------------------------------------
# 🔸 v. Collection Conversions

# list() – Convert to List
tupleData = (1, 2, 3)
listData = list(tupleData)
print(type(listData), listData)     # <class 'list'> [1, 2, 3]

# tuple() – Convert to Tuple
listData = [1, 2, 3]
tupleData = tuple(listData)
print(type(tupleData), tupleData)   # <class 'tuple'> (1, 2, 3)

# set() – Convert to Set
listData = [1, 2, 2, 3]
setData = set(listData)
print(type(setData), setData)       # <class 'set'> {1, 2, 3}
