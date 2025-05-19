# In Python, if/else statements are used to control the flow of your program based on conditions. Here’s a quick explanation and examples:

# 🔹 Basic if Statement

x = 10;
if x > 5 :
    print("X is greater than 5")

#  Another Exapmple

y = 20;
z = 10;
if y > z:
    print("y is gretaer than "+str(z))


# 🔹 if-else Statement

b = 8
a = 6
if a>b:
    print("a is greater than"+str(b))
else:
    print("a is less than"+str(b))

 # 🔹 if-elif-else Statement (multiple conditions)

carColor = "Blue"
if carColor == "Red":
    print("Car color is "+carColor)
elif carColor == "Blue":
    print("Car Color is "+carColor)
elif carColor =="Yellow":
    print("Car color is "+carColor)
else:
    print("Car color is Unkown")

# 🔹 Indentation Matters
# Python uses indentation (4 spaces by convention) to define code blocks:

if False:
    print("This will run")
    print("Still inside the if block")
print("Outside the if block")


# Create is  age project

age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif age >= 18 and age <= 50:
    print("You are an adult.")
else:
    print("You are old.")
