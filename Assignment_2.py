#---------------------------
# Multiple Line Comments
#---------------------------
# This is the second 
# lesson in the Python 
# course
#---------------------------

#---------------------------
# Variable name, age, country
#---------------------------
name = "Mohaned"
age = 39         
country ="Egypt" 

# name = str()
print(type(name))

# age = int()
print(type(age))

# country = str()
print(type(country))

#---------------------------
# Print A Separator Contains 20 Character
#---------------------------
n = "Python is an interpreted, high-level and general-purpose\
    programming language.Created by Guido van Rossum and first\
    released in 1991, Python is design philosophy emphasizes\
    code readability with its notable use of significant whitespace."

print(n.split())

#---------------------------
# Concatenate & Print
#---------------------------
print("Hello " + name + " Your Age Is " + str(age) + " & Country Is " + country)
# Another Solution
print("Hello {} Your Age Is {} & Country Is {}".format(name, age, country))
