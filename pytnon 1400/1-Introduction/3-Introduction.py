"""
Python Language 
Rewriting and summarizing by Hossein Jalili
1400-6-14
---------------------------------------------------------------------------------------------------
7-Namespaces and Scope in Python:

What is namespace:
A namespace is a system that has a unique name for each and every object in Python. 
An object might be a variable or a method. Python itself maintains a namespace in the form of a Python dictionary. 
Let’s go through an example, a directory-file system structure in computers. 
Needless to say, that one can have multiple directories having a file with the same name inside every directory. 
But one can get directed to the file, one wishes, just by specifying the absolute path to the file. 

Real-time example, the role of a namespace is like a surname. 
One might not find a single “Alice” in the class there might be multiple “Alice” 
but when you particularly ask for “Alice Lee” or “Alice Clark” (with a surname), 
there will be only one (time being don’t think of both first name and surname are same for multiple students).

On similar lines, the Python interpreter understands what exact method or variable one is trying to point to in the code, 
depending upon the namespace. So, the division of the word itself gives a little more information. 
Its Name (which means name, a unique identifier) + Space(which talks something related to scope). 
Here, a name might be of any Python method or variable and space depends upon the location from where is trying to access a variable or a method.

Types of namespaces :
When Python interpreter runs solely without any user-defined modules, methods, classes, etc. 
Some functions like print(), id() are always present, these are built-in namespaces. 
When a user creates a module, a global namespace gets created, later the creation of local functions creates the local namespace. 
The built-in namespace encompasses the global namespace and the global namespace encompasses the local namespace.

https://media.geeksforgeeks.org/wp-content/uploads/types_namespace-1.png

The lifetime of a namespace :
A lifetime of a namespace depends upon the scope of objects, if the scope of an object ends, the lifetime of that namespace comes to an end. 
Hence, it is not possible to access the inner namespace’s objects from an outer namespace.

"""
# var1 is in the global namespace
var1 = 5
def some_func():

	# var2 is in the local namespace
	var2 = 6
	def some_inner_func():

		# var3 is in the nested local
		# namespace
		var3 = 7

"""
As shown in the following figure, the same object name can be present in multiple namespaces as isolation between the same name is maintained by their namespace.

https://media.geeksforgeeks.org/wp-content/uploads/namespaces.png

But in some cases, one might be interested in updating or processing global variables only, 
as shown in the following example, one should mark it explicitly as global and the update or process.  
Note that the line “count = count +1” references the global variable and therefore uses the global variable, 
but compare this to the same line written “count = 1”.  Then the line “global count” is absolutely needed according to scope rules.

"""
# Python program processing
# global variable

count = 5
def some_method():
	global count
	count = count + 1
	print(count)
some_method()

# Output: 
# 6

"""
Scope of Objects in Python :
 
Scope refers to the coding region from which a particular Python object is accessible. 
Hence one cannot access any particular object from anywhere from the code, the accessing has to be allowed by the scope of the object.
Let’s take an example to have a detailed understanding of the same
"""
# Python program showing
# a scope of object

def some_func():
	print("Inside some_func")
	def some_inner_func():
		var = 10
		print("Inside inner function, value of var:",var)
	some_inner_func()
	#print("Try printing var from outer function: ",var)  
some_func()

# Output: 
# Inside some_func
# Inside inner function, value of var: 10

# Traceback (most recent call last):
#   File "/home/1eb47bb3eac2fa36d6bfe5d349dfcb84.py", line 8, in 
#     some_func()
#   File "/home/1eb47bb3eac2fa36d6bfe5d349dfcb84.py", line 7, in some_func
#     print("Try printing var from outer function: ",var)
# NameError: name 'var' is not defined

"""
---------------------------------------------------------------------------------------------------
8-Statement, Indentation and Comment in Python:

Statements
Instructions written in the source code for execution are called statements. 
There are different types of statements in the Python programming language like Assignment statements,
Conditional statements, Looping statements, etc. These all help the user to get the required output. 
For example, n = 50 is an assignment statement.

Multi-Line Statements: Statements in Python can be extended to one or more lines using parentheses (),
braces {}, square brackets [], semi-colon (;), continuation character slash (\). 
When the programmer needs to do long calculations and cannot fit his statements into one line, 
one can make use of these characters. 

    Example : 
    Declared using Continuation Character (\):
    s = 1 + 2 + 3 + \
        4 + 5 + 6 + \
        7 + 8 + 9

    Declared using parentheses () :
    n = (1 * 2 * 3 + 7 + 8 + 9)

    Declared using square brackets [] :
    footballer = ['MESSI',
            'NEYMAR',
            'SUAREZ']

    Declared using braces {} :
    x = {1 + 2 + 3 + 4 + 5 + 6 +
        7 + 8 + 9}

    Declared using semicolons(;) :
    flag = 2; ropes = 3; pole = 4


Indentation
A block is a combination of all these statements. 
Block can be regarded as the grouping of statements for a specific purpose. 
Most of the programming languages like C, C++, Java use braces { } to define a block of code. 
One of the distinctive features of Python is its use of indentation to highlighting the blocks of code. 
Whitespace is used for indentation in Python. 
All statements with the same distance to the right belong to the same block of code. 
If a block has to be more deeply nested, it is simply indented further to the right. 
You can understand it better by looking at the following lines of code:

"""
# Python program showing
# indentation

site = 'gfg'

if site == 'gfg':
	print('Logging on to geeksforgeeks...')
else:
	print('retype the URL.')
print('All set !')

# Output: 
# Logging on to geeksforgeeks...
# All set !

"""
The lines print(‘Logging on to geeksforgeeks…’) and print(‘retype the URL.’) are two separate code blocks. 
The two blocks of code in our example if-statement are both indented four spaces. 
The final print(‘All set!’) is not indented, and so it does not belong to the else-block. 

"""
j = 1
while(j<= 5):
	print(j)
	j = j + 1

# Output: 
# 1
# 2
# 3
# 4
# 5

"""
To indicate a block of code in Python, you must indent each line of the block by the same whitespace. 
The two lines of code in the while loop are both indented four spaces. 
It is required for indicating what block of code a statement belongs to. 
For example, j=1 and while(j<=5): is not indented, and so it is not within the while block. 
So, Python code structures by indentation.

Comments

Python developers often make use of the comment system as, without the use of it, things can get real confusing, real fast. 
Comments are the useful information that the developers provide to make the reader understand the source code. 
It explains the logic or a part of it used in the code. 
Comments are usually helpful to someone maintaining or enhancing your code when you are no longer around to answer questions about it. 
These are often cited as a useful programming convention that does not take part in the output of the program but improves the readability of the whole program. 
There are two types of comments in Python: 

Single line comments: Python single line comment starts with hashtag symbol with no white spaces (#) and lasts till the end of the line. 
If the comment exceeds one line then put a hashtag on the next line and continue the comment. 
Python’s single-line comments are proved useful for supplying short explanations for variables, function declarations, and expressions. 
See the following code snippet demonstrating single line comment:

"""
#Code 1: 
# This is a comment
# Print “GeeksforGeeks !” to console
print("GeeksforGeeks")

#Code 2: 
a, b = 1, 3 # Declaring two integers
sum = a + b # adding two integers
print(sum) # displaying the output

"""
Multi-line string as a comment: 
Python multi-line comment is a piece of text enclosed in a delimiter (“””) on each end of the comment. 
Again there should be no white space between delimiter (“””). 
They are useful when the comment text does not fit into one line; therefore need to span across lines.
Multi-line comments or paragraphs serve as documentation for others reading your code. 
See the following code snippet demonstrating multi-line comment:

"""
#Code 1: 
"""
This would be a multiline comment in Python that
spans several lines and describes geeksforgeeks.
A Computer Science portal for geeks. It contains
well written, well thought
and well-explained computer science
and programming articles,
quizzes and more.
…
"""
print("GeeksForGeeks")

#Code 2: 
'''This article on geeksforgeeks gives you a
perfect example of
multi-line comments'''

print("GeeksForGeeks")

"""
---------------------------------------------------------------------------------------------------
9-How to assign values to variables in Python and other languages:

This article discusses methods to assign values to variables. 

Method 1: Direct Initialisation Method 
--------------------------------------------
--------------------------------------------


"""
# Python 3 code to demonstrate variable assignment
# upon condition using Direct Initialisation Method

# initialising variable directly
a = 5

# printing value of a
print ("The value of a is: " + str(a))

# Output: 
# The value of a is: 5

"""
// C++ code to demonstrate variable assignment
// upon condition using Direct Initialisation Method

#include <bits/stdc++.h>
using namespace std;

int main()
{
	// initialising variables directly
	int a = 5;

	// printing value of a
	cout << "The value of a is: " << a;
}
--------------------------------------------
// C code to demonstrate variable assignment
// upon condition using Direct Initialisation Method

#include <stdio.h>

int main()
{
	// initialising variables directly
	int a = 5;

	// printing value of a
	printf("The value of a is: %d", a);
}
--------------------------------------------
// Java code to demonstrate variable assignment
// upon condition using Direct Initialisation Method

import java.io.*;

class GFG {
	public static void main(String args[])
	{

		// initialising variables directly
		int a = 5;

		// printing value of a
		System.out.println("The value of a is: " + a);
	}
}
--------------------------------------------
// C# code to demonstrate variable assignment
// upon condition using Direct Initialisation Method
using System;

class GFG{
	
public static void Main(String []args)
{
	
	// Initialising variables directly
	int a = 5;

	// Printing value of a
	Console.Write("The value of a is: " + a);
}
}

// This code is contributed by shivanisinghss2110
--------------------------------------------
<script>

// JavaScript code to demonstrate variable assignment
// upon condition using Direct Initialisation Method
		// initialising variables directly
		var a = 5;

		// printing value of a
		document.write("The value of a is: " + a);


</script>
// this code is contributed by shivanisinghss2110


Method 2: Using Conditional Operator (?:)
--------------------------------------------
--------------------------------------------


Below is the syntax in other popular languages.
"""
# Python3 code to demonstrate variable assignment
# upon condition using Conditional Operator

# Initialising variables using Conditional Operator
a = 1 if 20 > 10 else 0

# Printing value of a
print("The value of a is: " , str(a))

# This code is contributed by shivanisinghss2110

# Output: 
# The value of a is: 1

"""
// C++ code to demonstrate variable assignment
// upon condition using Conditional Operator

#include <bits/stdc++.h>
using namespace std;

int main()
{
	// initialising variables using Conditional Operator
	int a = 20 > 10 ? 1 : 0;

	// printing value of a
	cout << "The value of a is: " << a;
}
--------------------------------------------
// C code to demonstrate variable assignment
// upon condition using Conditional Operator

#include <stdio.h>

int main()
{
	// initialising variables using Conditional Operator
	int a = 20 > 10 ? 1 : 0;

	// printing value of a
	printf("The value of a is: %d", a);
}
--------------------------------------------
// Java code to demonstrate variable assignment
// upon condition using Conditional Operator

import java.io.*;

class GFG {
	public static void main(String args[])
	{

		// initialising variables using Conditional Operator
		int a = 20 > 10 ? 1 : 0;

		// printing value of a
		System.out.println("The value of a is: " + a);
	}
}
--------------------------------------------
// C# code to demonstrate variable assignment
// upon condition using Conditional Operator

using System;

class GFG {
	public static void Main(String []args)
	{

		// initialising variables using Conditional Operator
		int a = 20 > 10 ? 1 : 0;

		// printing value of a
		Console.Write("The value of a is: " + a);
	}
}
// this code is contributed by shivanisinghss2110
--------------------------------------------
<script>

// JavaScript code to demonstrate variable assignment
// upon condition using Conditional Operator

		// initialising variables using Conditional Operator
		var a = 20 > 10 ? 1 : 0;

		// printing value of a
		document.write("The value of a is: " + a);

// This code is contributed by shivanisinghss2110

</script>

--------------------------------------------
--------------------------------------------


One liner if-else instead of Conditional Operator (?:) in Python

"""
# Python 3 code to demonstrate variable assignment
# upon condition using One liner if-else

# initialising variable using Conditional Operator
# a = 20 > 10 ? 1 : 0 is not possible in Python
# Instead there is one liner if-else
a = 1 if 20 > 10 else 0

# printing value of a
print ("The value of a is: " + str(a))

# Output: 
# The value of a is: 1




