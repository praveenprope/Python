# ---------------------------------------------
# ✨ Variable Declaration
# ---------------------------------------------

myName = "Jhon Cena"
fatherName = "Big Smoke"
myAge = 25  # This is an integer

# ---------------------------------------------
# ❌ This will give an error (cannot add string and int)
# print("My Name is", myName, "And my Age is " + myAge)
# Error: TypeError: can only concatenate str (not "int") to str
# ---------------------------------------------

# ✅ Correct way using f-string (Recommended for clean formatting)
print(f"My name is {myName} and my age is {myAge}")

# ✅ Or convert the integer to a string manually
print("My father name is " + fatherName + " and his age " + str(myAge))

# ✅ Concatenating only strings works fine
print("My Name is " + myName + " And my father name is " + fatherName)

# ---------------------------------------------
# 🧾 Input and Output
# ---------------------------------------------

# Taking input from the user (input() always returns string)
userName = input("Enter Your Name: ")
userAge = input("Enter Your Age: ")

# ✅ This works perfectly because both are strings
print("My Name is " + userName + " and my age is " + userAge)
