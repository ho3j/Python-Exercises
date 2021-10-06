# print(a)               :NameError

s= 'ali'
# print(s + 2)           : TypeError

# s.append('reza')       :AttributeError

lst = [15, 20, 17]
# print(lst[3])          : IndexError

# print(lst + 4)         : TypeError
# lst.add(5)             : AttributeError

d = {'a' : 5 , 'b' : 6}
# print(d['f'])           : KeyError

# x = 8/0                 : ZeroDivisionError

print('-----')

try:
    print(k)
except NameError: 
    print('error')          # error
       
print('-----')

try:
    print(k)
except NameError as ne: 
    print(ne)              # name 'k' is not defined
    
print('-----')

s = 'ali'

try:
     print(s + 2)
except TypeError as te:    
    print(te)    # can only concatenate str (not "int") to str
    
    
print('-----')

try:
    x = 8 / 2
except ZeroDivisionError as ze:
    print(ze)            
else:
    print(x)      # 4
        
print('-----')

def divide(x, y):
    try:
        r = x / y
    except  ZeroDivisionError:
        print('error')
    else:
        print(r)
    finally:
        print('by')

divide(2, 1)       # 2.0     by   
divide(4, 0)       # error   by

print('-----')

s = '23'
try: 
   i = int(s)
except ValueError:
    i= -1
print(i)               # 23 
    

print('-----')

s = 'a'
try: 
   i = int(s)
except ValueError:
    i= -1
print(i)            # -1
    
print('-----')

def f(n):
    try:
        if n == 13:
            raise ValueError('unlucky number')
        return 20 / n
    except (ZeroDivisionError , TypeError):
        return 'Enter s number other than 0'

print(f(5))       # 4

print(f(0))       # Enter s number other than 0    

print(f('a'))     # Enter s number other than 0        

#print(f(13))      # unlucky number


print('-----')

# Nested try_except Blocks

try:
    print(5 / 0)
    try:
        print(n)
    except NameError  as ne:
        print(ne)
except ZeroDivisionError as ze:    
   print(ze)                         # division by zero
   
print('-----')

try:
    print(5 / 2)
    try:
        print(n)
    except NameError  as ne:
        print(ne)
except ZeroDivisionError as ze:    
   print(ze)
'''
2.5
name 'n' is not defined
'''

print('-----')

try :
    n = int(input('enter:'))
    assert n % 2 == 0
except:
    print('Not even')    
else:
    print( n * 2)    




    
    
    
    
    
    
    
    