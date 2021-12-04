# Name: Brian D. Yegerlehner
# Date: December 4th, 2021
# Title: Remove Any Given Character From String

# old and new string variable
string = "Hello, This is an Awesome String"

x = input("Please enter a character to eliminate from the string")

# Uses .replace to find and remove || replace character specified
string = string.replace(x, "")

# print old string
print(string)