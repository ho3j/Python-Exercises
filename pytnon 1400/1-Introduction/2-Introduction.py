"""
Python Language 
Rewriting and summarizing by Hossein Jalili
1400-6-14
---------------------------------------------------------------------------------------------------
5-Python 3 basics:

Python was developed by Guido van Rossum in the early 1990s and its latest version is 3.10.0, 
we can simply call it as Python3. Python 3.0 was released in 2008. 
and is interpreted language i.e it’s not compiled and the interpreter will check the code line by line.

So before moving on further.. 
let’s do the most popular ‘HelloWorld’ tradition 😛 and hence compare Python’s Syntax with C, C++, Java 
( I have taken these 3 because they are most famous and mostly used languages).

"""
# Python code for "Hello World"
# nothing else to type...see how simple is the syntax.

print("Hello World")   #Hello World

"""
Note: 
Please note that Python for its scope doesn’t depend on the braces ( { } ), 
instead it uses indentation for its scope.


1-If you are on Windows OS download Python by Clicking here and now install from the setup and in the start menu type IDLE.
IDLE, you can think it as an Python’s IDE to run the Python Scripts.

2-If you are on Linux/Unix-like just open the terminal and on 99% linux OS Python comes preinstalled with the OS.
Just type ‘python3’ in terminal and you are ready to go.

The ” >>> ” represents the python shell and its ready to take python commands and code.


In other programming languages like C, C++, and Java, 
you will need to declare the type of variables but 
in Python you don’t need to do that. 
Just type in the variable and when values will be given to it, 
then it will automatically know whether the value given would be an int, float, or char or even a String and boolean.

"""
# Python program to declare variables
myNumber = 3
print(myNumber)     

myNumber2 = 4.5
print(myNumber2)    

myNumber ="helloworld"
print(myNumber) 

myNumber =True
print(myNumber)  

# Output:
# 3
# 4.5
# helloworld
# True
"""
See, how simple is it, 
just create a variable and assign it any value you want and then use the print function to print it. 
Python have 4 types of built in Data Structures namely List, Dictionary, Tuple and Set.

'List' is the most basic Data Structure in python. 
List is a mutable data structure i.e items can be added to list later after the list creation. 
It’s like you are going to shop at the local market and made a list of some items and later on you can add more and more items to the list.
append() function is used to add data to the list.

"""
# Python program to illustrate a list

# creates a empty list
nums = []

# appending data in list
nums.append(21)
nums.append(40.5)
nums.append("String")

print(nums)

# Output:
# [21, 40.5, String]

"""
Comments:
# is used for single line comment in Python
"""
""" is used for multi line comments """

"""
Input and Output

In this section, we will learn how to take input from the user and hence manipulate it or simply display it. 
input() function is used to take input from the user.

"""
# Python program to illustrate
# getting input from user
name = input("Enter your name: ")

# user entered the name 'harssh'
print("hello", name)

# Output:
# hello harssh  



# Python3 program to get input from user

# accepting integer from the user
# the return type of input() function is string ,
# so we need to convert the input to integer
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

num3 = num1 * num2
print("Product is: ", num3)

# Output:
# Enter num1: 8 
# Enter num2: 6 
# Product is: 48

"""
Selection

You can think of functions like a bunch of code that is intended to do a particular task in the whole Python script. 
Python used the keyword ‘def’ to define a function.
Syntax:
    def function-name(arguments):
                #function body
"""
# Python program to illustrate
# functions
def hello():
	print("hello")
	print("hello again")
hello()

# calling function
hello()			

# Output:
# hello
# hello again
# hello
# hello again


"""
Now as we know any program starts from a ‘main’ 
function…lets create a main function like in many other programming languages.

"""
# Python program to illustrate
# function with main
def getInteger():
	result = int(input("Enter integer: "))
	return result

def Main():
	print("Started")

	# calling the getInteger function and
	# storing its returned value in the output variable
	output = getInteger()	
	print(output)

# now we are required to tell Python
# for 'Main' function existence
if __name__=="__main__":
	Main()

# Output:
# Started
# Enter integer: 5
# 5

"""
Iteration (Looping)

As the name suggests it calls repeating things again and again. 
We will use the most popular ‘for’ loop here.

"""
# Python program to illustrate
# a simple for loop

for step in range(5):	
	print(step)

# Output:
# 0
# 1
# 2
# 3
# 4

"""
Modules

Python has a very rich module library that has several functions to do many tasks.
‘import’ keyword is used to import a particular module into your python code. For instance consider the following program.

"""
# Python program to illustrate
# math module
import math

def Main():
	num = -85

	# fabs is used to get the absolute
	# value of a decimal
	num = math.fabs(num)
	print(num)
	
	
if __name__=="__main__":
	Main()

# Output:
# 85.0

"""
These are some of the most basics of the Python programming language.
---------------------------------------------------------------------------------------------------
6-Python Keywords:
Keywords in Python are reserved words that can not be used as a variable name, function name, or any other identifier.

Defining a Keyword:
In programming, a keyword is a “reserved word” by the language which conveys special meaning to the interpreter. 
It may be a command or a parameter. Keywords cannot be used as a variable name in the program snippet.

Keywords in Python:  
Python language also reserves some keywords that convey special meaning. 
Knowledge of these is a necessary part of learning this language. 
Below is a list of keywords registered by python. 

False, elif, lambda, 
None, else, nonlocal, 
True, except, not, 
and, finally, or, 
as, for, pass, 
assert, from, raise, 
break, global, return, 
class, if, try, 
continue, import, while 
def, in, with, 
del is, yield, 



We can also get all the keyword names using the below code.
Python Keywords List:
Sometimes, remembering all the keywords can be a difficult task while assigning variable names. 
Hence a function “kwlist()” is provided in the “keyword” module which prints all the 33 python keywords.

"""
# Python code to demonstrate working of iskeyword()

# importing "keyword" for keyword operations
import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)

# Output:
# The list of keywords is : 
# [‘False’, ‘None’, ‘True’, ‘and’, ‘as’, ‘assert’, ‘async’, ‘await’, ‘break’,
# ‘class’, ‘continue’, ‘def’, ‘del’, ‘elif’, ‘else’, ‘except’, ‘finally’, ‘for’,
# ‘from’, ‘global’, ‘if’, ‘import’, ‘in’, ‘is’, ‘lambda’, ‘nonlocal’, ‘not’,
# ‘or’, ‘pass’, ‘raise’, ‘return’, ‘try’, ‘while’, ‘with’, ‘yield’]

"""
How to check if a string is a keyword?

Python in its language defines an inbuilt module “keyword” which handles certain operations related to keywords. 
A function “iskeyword()” checks if a string is a keyword or not. 
Returns true if a string is a keyword, else returns false
"""
#Instead of writing this massive Python code
#we can also code this in a different way

#Python code to demonstrate working of iskeyword()

# importing "keyword" for keyword operations
import keyword
import keyword
# initializing strings for testing while putting them in an array
keys = ["for", "while", "tanisha", "break", "sky",
"elif", "assert", "pulkit", "lambda", "else", "sakshar"]

for i in range(len(keys)):
	# checking which are keywords
	if keyword.iskeyword(keys[i]):
		print(keys[i] + " is python keyword")
	else:
		print(keys[i] + " is not a python keyword")

# Output: 
# for is a python keyword
# geeksforgeeks is not a python keyword
# elif is a python keyword
# elseif is not a python keyword
# nikhil is not a python keyword
# assert is a python keyword
# shambhavi is not a python keyword
# True is a python keyword
# False is a python keyword
# akshat is not a python keyword
# akash is not a python keyword
# break is a python keyword
# ashty is not a python keyword
# lambda is a python keyword
# suman is not a python keyword
# try is a python keyword
# vaishnavi is not a python keyword

"""
Let’s discuss each keyword in detail with the help of good examples.

True, False, None :

True: This keyword is used to represent a boolean true. If a statement is true, “True” is printed.
False: This keyword is used to represent a boolean false. If a statement is false, “False” is printed. 
None: This is a special constant used to denote a null value or a void. It’s important to remember, 0, any empty container(e.g empty list) does not compute to None. 
It is an object of its datatype – NoneType. It is not possible to create multiple None objects and can assign them to variables.
"""
print(False == 0)
print(True == 1)

print(True + True + True)
print(True + False + False)

print(None == 0)
print(None == [])

# Output
# True
# True
# 3
# 1
# False
# False

"""
and, or, not, in, is

and: This a logical operator in python. “and” Return the first false value. 
If not found return last. The truth table for “and” is depicted below. 
https://media.geeksforgeeks.org/wp-content/uploads/and1-249x300.png

The expression x and y first evaluates x; if x is false, its value is returned; 
otherwise, y is evaluated and the resulting value is returned.

The expression x or y first evaluates x; if x is true, its value is returned; 
otherwise, y is evaluated and the resulting value is returned.

or: This a logical operator in python. “or” Return the first True value.
if not found return last. The truth table for “or” is depicted below. 
https://media.geeksforgeeks.org/wp-content/uploads/or1-250x300.png

not: This logical operator inverts the truth value. The truth table for “not” is depicted below. 
in: This keyword is used to check if a container contains a value. This keyword is also used to loop through the container.
is: This keyword is used to test object identity, i.e to check if both the objects take the same memory location or not. 
"""
# showing logical operation
# or (returns True)
print(True or False)

# showing logical operation
# and (returns False)
print(False and True)

# showing logical operation
# not (returns False)
print(not True)

# using "in" to check
if 's' in 'geeksforgeeks':
	print("s is part of geeksforgeeks")
else:
	print("s is not part of geeksforgeeks")

# using "in" to loop through
for i in 'geeksforgeeks':
	print(i, end=" ")

print("\r")

# using is to check object identity
# string is immutable( cannot be changed once allocated)
# hence occupy same memory location
print(' ' is ' ')

# using is to check object identity
# dictionary is mutable( can be changed once allocated)
# hence occupy different memory location
print({} is {})

# Output: 
# True
# False
# False
# s is part of geeksforgeeks
# g e e k s f o r g e e k s 
# True
# False

"""
Iteration Keywords – for, while, break, continue:

for: This keyword is used to control flow and for looping.
while: Has a similar working like “for”, used to control flow and for looping.
break: “break” is used to control the flow of the loop. The statement is used to break out of the loop and passes the control to the statement following immediately after loop.
continue: “continue” is also used to control the flow of code. The keyword skips the current iteration of the loop but does not end the loop.

"""
# Using for loop
for i in range(10):

	print(i, end = " ")
	
	# break the loop as soon it sees 6
	if i == 6:
		break
	
print()
	
# loop from 1 to 10
i = 0
while i <10:
	
	# If i is equals to 6,
	# continue to next iteration
	# without printing
	if i == 6:
		i+= 1
		continue
	else:
		# otherwise print the value
		# of i
		print(i, end = " ")
	i += 1

# Output
# 0 1 2 3 4 5 6 
# 0 1 2 3 4 5 7 8 9 

"""
Condtional keywords – if, else, elif:

if : It is a control statement for decision making. Truth expression forces control to go in “if” statement block.
else : It is a control statement for decision making. False expression forces control to go in “else” statement block.
elif : It is a control statement for decision making. It is short for “else if“
"""

# Python program to illustrate if-elif-else ladder
#!/usr/bin/python

i = 20
if (i == 10):
	print ("i is 10")
elif (i == 20):
	print ("i is 20")
else:
	print ("i is not present")

# Output
# i is 20

"""
def

def keyword is used to declare user defined functions.
"""
# def keyword
def fun():
	print("Inside Function")
	
fun()

# Output:
# Inside Function

"""
Return Keywords – Return, Yield

return : This keyword is used to return from the function.
yield : This keyword is used like return statement but is used to return a generator.
"""

# Return keyword
def fun():
	S = 0
	
	for i in range(10):
		S += i
	return S

print(fun())

# Yield Keyword
def fun():
	S = 0
	
	for i in range(10):
		S += i
		yield S

for i in fun():
	print(i)

# Output
# 45
# 0
# 1
# 3
# 6
# 10
# 15
# 21
# 28
# 36
# 45

"""
class

class keyword is used to declare user defined classes.
"""
# Python3 program to
# demonstrate instantiating
# a class

class Dog:
	
	# A simple class
	# attribute
	attr1 = "mammal"
	attr2 = "dog"

	# A sample method
	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)

# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()

# Output
# mammal
# I'm a mammal
# I'm a dog

"""
With

with keyword is used to wrap the execution of block of code within methods defined by context manager.
This keyword is not used much in day to day programming.
"""
# using with statement
with open('file_path', 'w') as file:
	file.write('hello world !')

"""
as

as keyword is used to create the alias for the module imported. 
i.e giving a new name to the imported module. E.g import math as mymath.
"""
import math as gfg

print(gfg.factorial(5))

# Output
# 120

"""
pass

pass is the null statement in python. Nothing happens when this is encountered. 
This is used to prevent indentation errors and used as a placeholder
"""
n = 10
for i in range(n):
# pass can be used as placeholder
# when code is to added later
	pass

"""
Lambda

Lambda keyword is used to make inline returning functions with no statements allowed internally. 
"""
# Lambda keyword
g = lambda x: x*x*x

print(g(7))

# Output
# 343

"""
Import, From

import : This statement is used to include a particular module into current program.
from : Generally used with import, from is used to import particular functionality from the module imported.
"""
# import keyword
import math
print(math.factorial(10))

# from keyword
from math import factorial
print(factorial(10))

# Output
# 3628800
# 3628800

"""
Exception Handling Keywords – try, except, raise, finally, and assert

try : This keyword is used for exception handling, used to catch the errors in the code using the keyword except. Code in “try” block is checked, if there is any type of error, except block is executed.
except : As explained above, this works together with “try” to catch exceptions.
finally : No matter what is result of the “try” block, block termed “finally” is always executed.
raise: We can raise an exception explicitly with the raise keyword
assert: This function is used for debugging purposes. Usually used to check the correctness of code. If a statement is evaluated to be true, nothing happens, but when it is false, “AssertionError” is raised. One can also print a message with the error, separated by a comma.
"""

# initializing number
a = 4
b = 0

# No exception Exception raised in try block
try:
	k = a//b # raises divide by zero exception.
	print(k)

# handles zerodivision exception
except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')

# assert Keyword
# using assert to check for 0
print ("The value of a / b is : ")
assert b != 0, "Divide by 0 error"
print (a / b)

# Output
# Can't divide by zero
# This is always executed
# The value of a / b is :
# AssertionError: Divide by 0 error

"""
del

del is used to delete a reference to an object. Any variable or list value can be deleted using del.
"""
my_variable1 = 20
my_variable2 = "GeeksForGeeks"

# check if my_variable1 and my_variable2 exists
print(my_variable1)
print(my_variable2)

# delete both the variables
del my_variable1
del my_variable2

# check if my_variable1 and my_variable2 exists
print(my_variable1)
print(my_variable2)

# Output
# 20
# GeeksForGeeks
# NameError: name 'my_variable1' is not defined

"""
Global, Nonlocal

global: This keyword is used to define a variable inside the function to be of a global scope.
non-local : This keyword works similar to the global, but rather than global, this keyword declares a variable to point to variable of outside enclosing function, in case of nested functions.
"""

# global variable
a = 15
b = 10

# function to perform addition
def add():
	c = a + b
	print(c)

# calling a function
add()

# nonlocal keyword
def fun():
	var1 = 10

	def gun():
		# tell python explicitly that it
		# has to access var1 initialized
		# in fun on line 2
		# using the keyword nonlocal
		nonlocal var1
		
		var1 = var1 + 10
		print(var1)

	gun()
fun()


# Output
# 25
# 20

