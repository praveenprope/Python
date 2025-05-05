# 4. Mapping Type: dict
# 5. Set Types: set, frozenset


# 4. Mapping Type: dict

MarvelSuperHero = {
    "Name": "SpiderMan",
    "RealName": "PeterParker",
    "Rank": 1,
    "Address": "NewYorkCity"  # Fixed the spelling of "Address"
}

print(MarvelSuperHero)

# 1. Accessing values:

print(MarvelSuperHero["Address"])  # Fixed spelling of "Address"

# 2. Adding/Updating:

# i. Updating

MarvelSuperHero["Rank"] = 4
print(MarvelSuperHero)

# ii. Adding

MarvelSuperHero["Country"] = "USA"
print(MarvelSuperHero["Country"])

# Deleting Dict

del MarvelSuperHero["RealName"]
print(MarvelSuperHero)

# Iterating:

for key, value in MarvelSuperHero.items():
    print(key, value)

# Methods

print("MarvelSuperHeroesAllKeys", MarvelSuperHero.keys())  # Fixed the spelling of "Keys"
print("MarvelSuperHeroesAllValues", MarvelSuperHero.values())
print("MarvelSuperHeroesAllItems", MarvelSuperHero.items())

# 5. Set Types: set, frozenset
# In Python, Set Types are used to store multiple unique items in a single variable. There are two main set types: i. set, ii. frozenset

# i. set
# A set is an unordered, mutable collection of unique elements.

twoTable = {2, 4, 6, 8, 10}
threeTable = {3, 6, 9, 9, 12, 15}

print(twoTable)
print(threeTable)  # Duplicates are removed, output -> {3, 6, 9, 12, 15}

# Key Features of set:

# i. No duplicate elements
# ii. Unordered (no indexing or slicing)
# iii. Mutable (you can add or remove items)
# iv. Elements must be immutable (e.g., numbers, strings, tuples)

# 🔹 Common Operations:

fiveTable = {5, 10, 15, 10, 25, 30, 35, 40}
print(fiveTable)

fiveTable.add(45)
print(fiveTable)

fiveTable.update([55, 60])
print(fiveTable)

fiveTable.remove(5)
print(fiveTable)

# Set Operations (like in Math):

tenTable = {10, 20, 30, 40, 50, 60}
twentyTable = {20, 40, 60, 80, 100, 120}

print(tenTable.union(twentyTable))

# The intersection() method returns only the common elements between both sets.
print(tenTable.intersection(twentyTable))

# tenTable.difference(twentyTable) returns all elements that are in tenTable but NOT in twentyTable.
print(tenTable.difference(twentyTable))

# It returns elements that are in either one of the sets, but not in both (i.e., removes common elements).
print(tenTable.symmetric_difference(twentyTable))

# ⚖️ Step-by-Step:
# Common elements: 20, 40, 60 ❌ (removed)
# Unique to tenTable: 10, 30, 50
# Unique to twentyTable: 80, 100, 120

# ii. frozenset

fourTable = frozenset([4, 8, 12, 16, 20])
sixTable = frozenset([6, 12, 18, 24, 30])

print(fourTable.union(sixTable))
print(fourTable.intersection(sixTable))

# Key Features of frozenset:
# Immutable (no add or remove)
# Can be used as a dictionary key or element of another set
# Supports all set operations like union, intersection, etc.

# | Feature           | `set` | `frozenset` |
# | ----------------- | ----- | ----------- |
# | Mutable           | ✅ Yes | ❌ No        |
# | Hashable          | ❌ No  | ✅ Yes       |
# | Allows Duplicates | ❌ No  | ❌ No        |
# | Set Operations    | ✅ Yes | ✅ Yes       |
