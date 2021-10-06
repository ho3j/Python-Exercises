"""
Operators :
    Arithmetic : +,-,*,/,%,**,//   
    Assignment : =,+=,-=,*= ,/= ,%= ,//= ,**= 
    Comparison : ==,!=,>,<,>=,<=
    Logical    : and, or, not
    Membership : in , not in
    Bitwise    :  &, |, ^, ~, <<, >>

    Walrus operator:    :=      is the == or = in Python
"""
################################
print(num := 15)
# num <-- 15     and print 15 in output
################################

print('Arithmetic Operators')

#Addition
print(1 + 3)       # 4

#Subtraction
print(5 - 3)       # 2

#Multiplication
print(2 * 3)       # 6

#Float Division
print(3 / 2)       # 1.5
 
#Integer Division
print(3 // 2)      # 1

#Remainder
print(17 % 5)      # 2

# Exponentiation
print(2 ** 3)      # 8 
print(0 ** 0)      # 1
print(6 ** 0)      # 1
print(0 ** 2)      # 0

####################################################

print('Operator Precedence')

print(8 - 2 * 3)                    # 2   : (8 - (2 * 3))
print(1 + 3 * 4 / 2)                # 7.0 : (1 + (3 * 4) / 2)
print(16 / 2 ** 3)                  # 2.0 : (16 / (2 ** 3))
print(2**2**3)                      # 256 : ** r to l : (2**(2**3)) 

####################################################

print('Augmented Assignment Operator')

x = 4
x += 2    # x = x + 2
print(x)  # 6

y = 8
y //= 2   # y = y // 2
print(y)  # 4

####################################################

print('Comparison Operators')

print(2 == 3)                       # False
print(2 != 3)                       # True
print(2 < 3)                        # True

print('Logical Operators') 

print(1<3  or 4>5)                  # True
print(1<3 and 4>5)                  # False
print(not 1<3)                      # False

# 'Short-circuit'
print(1 >= 2 and (5/0) > 2)         # False

#print(3 >= 2 and (5/0) > 2)        # division by zero

####################################################

print('Membership Operators')

x = [1,2,3,4,5]
print(3 in x)                       # True
print(24 not in x)                  # True

####################################################

print('Bitwise Operators')

a = 13
print(bin(a))                       # 1101

b = 14
print(bin(b))                       # 1110

###

c = a | b
print(bin(c))                      # 1111

###

c = a & b
print(bin(c))                      # 1100

###

c= a ^ b
print(bin(c))                      # 0011 

###

a = 13
print(a << 1)                      # 26

###

a = 20
print(a >> 1)                     # 10

###

a = 18
print(a >> 2)                     # 4

####################################################

print('--- Operations on string ---')

s1 = 'Farshid'
s2 = ' Shirafkan'
s3 = s1 + s2
print(s3)                        # Farshid Shirafkan

###

s = 'sara'
print(2*s)                       # sarasara

####################################################

#Every object in python is stored somewhere in memory. 
#We can use id() to get that memory address.

s1 = 'farshid'
s2 = 'farshid'
print(id(s1))             #2866185855344
print(id(s1)==id(s2))            # True

s1 += ' shirafkan'

print(id(s1)==id(s2))            # False
##############################################
# dir
dir(list)

"""
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
 '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', 
 '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
 '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
  '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 
  'remove', 'reverse', 'sort']
"""
print(list.__doc__)

"""
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.
"""
###############################################
print()    #because a free line

print(abs(-4))             # 4
print(pow(2,3))            # 8
print(divmod(8,4))         # (2,0)
print(round(2.6))          # 3
print(round(2.5))          # 2
print(abs.__doc__)         # 'Return the absolute value of the argument.' 

print('# math #')

import math
print( math.sqrt(4))       #2.0
print( math.trunc(2.3))    #2
print( math.floor(2.3))    #2
print( math.ceil(2.3))     #3
print( math.factorial(4))  #24
print( math.log2(32))      #5.0
print( math.log10(100))    #2.0
print( math.e)             #2.7
print( math.log(32))       #3.46   paye e
print( math.sin(5))        #-0.9
print( math.cos(5))        #0.28
print( math.fmod(9,4))     #1.0
print( math.gcd(30,4))     #2   bmm
print( math.lcm(30,4))     #60  kmm

print( math.fabs(-4))      #4.0   float
print( abs(-4))            #4     int
print( math.pow(2,3))      #8.0   float
print( pow(2,3))           #8     int
print( math.pi)            # 3.141592653589793

print(f'{math.pi :.2f}')   # 3.14
print(f'{math.pi :.25f}')  # 3.1415926535897931159979635
print(f'{math.pi :15.2f}') #            3.14

print('# random #')
import random
print( random.randint(1, 5))  #2 or...1..3..4..5
print( random.choice([1,5]))  #5 or 1
print( random.randrange(0,10)) #0 or ...9   not 10

a = [1,2,3,4]
random.shuffle(a)             #bor [4, 3, 2, 1] or [4, 1, 3, 2] or...
print(a)

print('# datetime #')

import datetime
now = datetime.datetime.now()
print(now)                     # 2021-07-01 23:16:50.582192
print( now.year)               # 2021
print( now.month)              # 7
print( now.day)                # 1
print( now.hour)               # 23
print( now.second)             # 16 or 17 ---> up 59



print('# sys , platform ,os #')
import sys
print( sys.version)           # 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)]

print( sys.platform)          # win32

import platform
platform.release()            # 10    windows10

import os 
print(os.getcwd())            # C:\Users\ho3j\Desktop\py_sample_code
