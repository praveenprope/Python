# What is a String?
# A string is a sequence of characters enclosed in single (') or double (") quotes.

name = "Virat Kholi"
print(name)

# ✅ 1. Concatenation (Joining Strings)

famousName = "Narendra Modi"
job = "Prime Minister"
print(job+" "+famousName)

#  ✅ 2. Repetition

print((famousName+" ")*3)

# ✅ 3. Accessing Characters (Indexing)

print(job[0])
print(job[2])
print(job[-1])

# ✅ 4. Slicing Strings

print(famousName[0:8])
print(famousName[9:])

# ✅ 5. Length of a String

print(len(famousName))

# lower()	Converts to lowercase

print(name.lower())
print(name.upper())

# strip()	Removes surrounding whitespace

fotballPlayerName = "  Messi  "
print(fotballPlayerName)
print(fotballPlayerName.strip())

# replace()	Replace substring

print(fotballPlayerName.replace("M","L"))


# split()	Splits into list

cricketPlayerName = "M,S ,D,h,o,n,i"
print(cricketPlayerName.split(","))

