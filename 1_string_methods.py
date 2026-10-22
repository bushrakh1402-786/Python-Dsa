==========================================
 STRING METHODS - 42 TOPIC SEQUENCE
==========================================

# Method 1. len()
# Returns the number of characters in a string.

name = "Bushra"

result = len(name)

print(result)

# Output:
# 6
           
len(s)       # number of characters
s[0]         # first character
s[len(s)-1]  # last character



# Method 2. lower()

# lower() converts all uppercase letters into lowercase.

# Example 1
name = "BUSHRA"
print(name.lower())

# Example 2: Mixed case
text = "PyThOn"
print(text.lower())



#output
bushra
python
google 

# Method 3. upper()
# upper() converts lowercase letters into uppercase letters.

# Example 1: Basic use
text = "python"
print(text.upper())


# Example 2: Mixed case
name = "BuShRa"
print(name.upper())


# Example 3: Numbers and symbols remain unchanged
value = "python123!"
print(value.upper())


# Example 4: Original string is not changed
s = "Google"
result = s.upper()

print(s)
print(result)


# Example 5: Case-insensitive comparison
a = "google"
b = "GOOGLE"

print(a.upper() == b.upper())

#PYTHON
BUSHRA
PYTHON123!
Google
GOOGLE
True


 #Method 4: capitalize()

# Definition:
# First character uppercase aur baaki characters lowercase ho jaate hain.

# Syntax:
# string.capitalize()


# Example 1
text = "hello world"
print(text.capitalize())

# Output: Hello world


# Example 2
text = "hELLO PYTHON"
print(text.capitalize())

# Output: Hello python

   #Method 5 :tittle()

# Definition:
# title() method har word ke first character ko
# uppercase aur baaki characters ko lowercase banata hai.

# Syntax:
# string.title()


# Example 1
text = "hello world"
print(text.title())

# Output: Hello World


# Example 2
text = "welcome to python"
print(text.title())

# Output: Welcome To Python

#Method 6: swapcase()


# Definition:
# Converts uppercase letters to lowercase
# and lowercase letters to uppercase.

# Syntax:
# string.swapcase()


# Example 1
text = "Hello World"
print(text.swapcase())

# Output: hELLO wORLD


# Example 2
text = "PYTHON dsa"
print(text.swapcase())

# Output: python DSA


# Method 7: casefold()

# Definition:
# casefold() string ko lowercase mein convert karta hai.
# Ye case-insensitive string comparison ke liye useful hai.

# Syntax:
# string.casefold()


# Example 1
text = "HELLO WORLD"
print(text.casefold())

# Output: hello world


# Example 2
text1 = "Python"
text2 = "PYTHON"

print(text1.casefold() == text2.casefold())

# Output: True


# Method 8: find()

# Definition:
# find() method string mein substring ki position return karta hai.
# Agar substring nahi milti, toh -1 return karta hai.

# Syntax:
# string.find(substring)


# Example 1
text = "hello world"
print(text.find("world"))

# Output: 6


# Example 2
text = "banana"
print(text.find("na"))

# Output: 2



# Method 9: index()

# Definition:
# index() method substring ki first occurrence ka index return karta hai.
# Agar substring nahi milti, toh ValueError raise hota hai.

# Syntax:
# string.index(substring)


# Example 1
text = "hello world"
print(text.index("world"))

# Output: 6


# Example 2
text = "banana"
print(text.index("na"))

# Output: 2


# Method 10: rfind()

# Definition:
# rfind() returns the index of the last occurrence
# of a substring. If not found, it returns -1.

# Syntax:
# string.rfind(substring)


# Example 1
text = "hello hello"
print(text.rfind("hello"))

# Output: 6


# Example 2
text = "banana"
print(text.rfind("na"))

# Output: 4



# Method 11: rindex()

# Definition:
# rindex() returns the index of the last occurrence
# of a substring. If not found, it raises ValueError.

# Syntax:
# string.rindex(substring)


# Example 1
text = "hello hello"
print(text.rindex("hello"))

# Output: 6


# Example 2
text = "banana"
print(text.rindex("na"))

# Output: 4




# Method 12: count()

# Definition:
# count() returns the number of non-overlapping
# occurrences of a substring in a string.

# Syntax:
# string.count(substring)


# Example 1
text = "banana"
print(text.count("a"))

# Output: 3


# Example 2
text = "mississippi"
print(text.count("ss"))

# Output: 2



# 13. startswith() Method

# Example 1
text = "Google Placement"
print(text.startswith("Google")) 

 # Output: True

# Example 2
text = "Python Programming"
print(text.startswith("Programming"))  


# Output: False



# Method : 14
# Method: endswith()
# Google Placement 2027

filename = "hello.py"
print(filename.endswith(".py"))
# Output: True

website = "google.com"
print(website.endswith(".in"))
# Output: False




# Method 15: split()
# DSA Preparation - Google Placement 2027

# split() divides a string into a list of substrings.

# Example 1: Split by whitespace
text = "Google DSA Preparation"
print(text.split())
# Output: ['Google', 'DSA', 'Preparation']

# Example 2: Split by comma
languages = "Python,Java,C++"
print(languages.split(","))
# Output: ['Python', 'Java', 'C++']

# Time Complexity: O(n)
# Auxiliary Space: O(n)




# Method 18: rsplit()
# DSA Preparation - Google Placement 2027

# rsplit() splits a string from the right
# and returns a list.

# Example 1: Split once from the right
text = "apple-banana-mango"
print(text.rsplit("-", 1))
# Output: ['apple-banana', 'mango']

# Example 2: Split using whitespace
text = "Python Java C++"
print(text.rsplit())
# Output: ['Python', 'Java', 'C++']

# Time Complexity: O(n)
# Auxiliary Space: O(n)







