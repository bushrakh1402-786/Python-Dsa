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

#Method 6: 
