# 6. Boolean Type: bool
# 7. Binary Types: bytes, bytearray, memoryview
# 8. None Type: NoneType

# 6. Boolean Type: bool

isSchoolOpen = True
print(isSchoolOpen)

isCollegeOpen = False
print(isCollegeOpen)

# True = 1, False = 0

# 7. Binary Types: bytes, bytearray, memoryview
# These types are used to handle binary data, such as files, images, or network data.

# i. bytes
# - Immutable sequence of bytes (cannot be changed)
# - Often used to represent binary data like encoded strings

data = bytes([65])
print(data)          # Output: b'A'

stringData = "A".encode()
print(stringData)    # Output: b'A'

# ii. bytearray
# - Mutable version of bytes
# - You can modify its contents

data = bytearray([65, 66, 67])
print(data)          # Output: bytearray(b'ABC')

data[1] = 68
print(data)          # Output: bytearray(b'ADC')

# iii. memoryview
# - A view object that lets you access the internal data of an object (like bytes or bytearray) without copying it
# - Very useful for performance when working with large binary data

data = bytearray([10, 20, 30, 40])
view = memoryview(data)

print(view[1])       # Output: 20
view[1] = 25
print(data)          # Output: bytearray(b'\n\x19\x1e(')

# | Type         | Mutable | Use Case                         | Example         |
# | ------------ | ------- | -------------------------------- | --------------- |
# | `bytes`      | ❌ No    | Read-only binary data            | b"Hello"        |
# | `bytearray`  | ✅ Yes   | Modify binary data               | bytearray(b"A") |
# | `memoryview` | ✅ Yes   | Work with large data efficiently | memoryview(obj) |


# ✅ 8. None Type: NoneType


# 🔹 What is None?
# None is a special constant in Python.
# It represents the absence of a value or a null value.
# Type of None is NoneType.

x = None
print(x)             # Output: None
print(type(x))       # Output: <class 'NoneType'>
