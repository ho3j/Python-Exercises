# Data Types   
'''
    int
    float
    str
    complex
    bool
'''
i = 5                
print(type(i))      # <class 'int'>

print('------')

f = 3.6       
print(type(f))      # <class 'float'>

print('------')

s = "Python"  
print(type(s))      # <class 'str'>

print('------')

c = 2 + 7j          
print(type(c))      # <class 'complex'>

print('------')

b = True       
print(type(b))      # <class 'bool'>

print('--variable names---')

print('a2'.isidentifier())      # True
print('2a'.isidentifier())      # False
print('_myvar'.isidentifier())  # True
print('my_var'.isidentifier())  # True
print('my$'.isidentifier())     # False

from keyword import iskeyword
print( iskeyword('if'))         # True

print('---Python Casting---')

i = 4
print(float(i))     # 4.0

print('------')

s ='15'
print(int(s) + 1)   # 16

print('------')

x = 4         
y = 8         
y, x = x, y         # assign y value to x and x value to y
print(x)            # 8
print(y)            # 4

print('------')

a = 1
b = 2
a, b = b, a + b
print(a)           # 2
print(b)           # 3 

print('------')

###################################################################
# Operators :

'''
Operators :
    Arithmetic : +,-,*,/,%,**,//   
    Assignment : =,+=,-=,*= ,/= ,%= ,//= ,**= 
    Comparison : ==,!=,>,<,>=,<=
    Logical    : and, or, not
    Membership : in , not in
    Bitwise    :  &, |, ^, ~, <<, >>
'''

print(17 // 2)         # 8
print(17 % 2)          # 1
print(3 ** 2)          # 9

print('------')

y = 4
y //= 2               # y = y // 2
print(y)              # 2

print('------')

print(2 != 3)                       # True

print('------')

print(1<3 and 4>5)                  # False

print('------')

a = 15
print(bin(a))                       # 0b1111
b = 9
print(bin(b))                       # 0b1001
c = a | b
print(bin(c))                       # 0b1111

print('------')
print('# math #')
import math
print( math.sqrt(16))      # 4.0
print( math.trunc(4.3))    # 4
print( math.factorial(3))  # 6
print( math.log2(16))      # 4.0
print( math.fmod(17,2))    # 1.0
print( math.fabs(-5))      # 5.0
print( math.pow(2,4))      # 16.0
print( math.pi)            # 3.141592653589793

print('# random #')
import random
print( random.randint(1, 10))  
print( random.choice([1,10]))  

print('# datetime #')
import datetime
now = datetime.datetime.now()
print(now)                 # 2020-05-20 03:20:13.384938

###################################################################

'''
Control statements:
    if
    if else
    elif
'''
import math
n = -9
if n < 0 :
   n = abs(n)
   
print(math.sqrt(n))        # 3.0

print('------')

a = 9
if a % 2 == 0:
    print('evevn')                  
else:    
    print('odd')         # odd

print('------')
print('conditional expression')

a = 3
b = 8

#if a < b:
#    m = a
#else:
#    m = b

m = a if a < b else b    

print(m)                 # 3

print('------')

grade = 7
s = 'fail' if grade < 10 else 'pass'
print(s)                                # fail

print('------')

today = 'holiday'
b = 40

if today == 'holiday':
   if b > 50:
       print('shopping')              
   else:
       print('watch TV')               # watch TV
else:
    print('normal working day')   

print('------')

score = 82

if score >= 90:
    l = 'A'
else:
  if score >= 80 :
      l = 'B'
  else:
       if score>= 70:
           l = 'C'
       else :
           l = 'D'

print(l)         # B
# or   
if score >= 90:
    l = 'A'
elif score >= 80 :
    l = 'B'
elif score>= 70:
    l = 'C'
else :
    l = 'D'

###################################################################

"""
    loop : 
          for 
          while
"""

for i in range(3):
    print(i , end = ' ')      # 0 1 2 
    
for _ in range(3):
    print('hello')      
    
print('\n------')

for j in range(6,11,2):
    print(j , end = ' ' )    # 6 8 10

print('\n------')

for i in range(2,5):
    for j in range(1,i):
        print(j , end = ' ')
    print()        

'''
1
1  2
1  2  3
'''
    
print('\n # break #')    

for i in range(6):
    if i == 4 :
        break
    else:
        print(i,end=' ')   # 0 1 2 3


print('\n # continue #')    

for i in range(6):
    if i == 4 :
        continue
    else:
        print(i,end=' ')   # 0 1 2 3 5

print('\n # while #')
      
i = 1      
while i <= 4:
    print(i , end= ' ')    # 1 2 3 4
    i += 1

print('\n------')

n = 9
while n > 2:
    n -= 1
    if n == 4:
        break
    print(n , end = ' ')    # 8 7 6 5
    
print('\n------')

n = 9
while n > 2:
    n -= 1
    if n == 4:
        continue
    print(n , end = ' ')    # 8 7 6 5 3 2 
    
    
#############################################################################
'''
  string
        len , is..  ,find , count  , title , ljust , startswith , replcae , 
        strip , split , join , format , ...
'''
print('\n---String---')    

s = 'python'

print(len(s))               # 6
print( 'th' in s)           # True

print(s.islower())          # True 
print(s.isalpha())          # True
print(s.isdigit())          # False

print(s.find('o'))          # 4
print(s.count('o'))         # 1

print(s.title())            # Python
print(s.upper())            # PYTHON

print(s.ljust(8,'+'))       # python++
print(s.startswith('py'))   # True

print(s.replace('thon','ramid'))   # pyramid

print('------')

s = '$python$$'
print(s.strip('$'))     # python

print('------')

s = 'Python created by Rossum'
a = s.split(' ')
print(a)            # ['Python', 'created', 'by', 'Rossum']

print('------')

b = ['Python', 'created', 'by', 'Rossum']
c =' '.join(b)
print(c)

print('------')
print('# format #')
      
s = 'python'

print(f'name : {s}')           # name : python
print('name:{}'.format(s))     # name : python      

print('------')

a = 'farshid'
b = 'shirafkan'

print('name:{0}   family:{1}'.format(a, b))  

# name:farshid   family:shirafkan

print('------')

a = 15
b = 17.9999

print('{:d} {:.1f}'.format(a, b))    # 15  18.0

print('------')

###################################################################

"""
    list
    'index' ,'count','insert','remove','pop','reverse' , 'sort' ,'extend'
    , 'append','clear','copy',...
    
"""

a = [8, 2, 12]

print(type(a))      # <class 'list'>

print(len(a))       # 3

print(a.index(2))   # 1

print(a[1])         # 2
a[1] = 7            # list is mutable

print('------')

a = [13, 5, 30, 8, 6, 25]

print(a[1:4])        # [5, 30, 8]
print(a[0:3])        # [13, 5, 30]
print(a[3:])         # [8, 6, 25]
print(a[::-1])       # [25, 6, 8, 30, 5, 13]

print(a[0:7:2])      # [13, 30, 6]

print('------')

child = ['sara','mahsa']
for i in child:
    print(i)

# or 
for i in range(len(child)):
    print(child[i])

print('------')

a = [3, 5]
b = a*2
print(b)           # [3, 5, 3, 5]

print('------')

a = [1, 2 , 3]
b = ['a', 'b']
c = a + b
print(c)           # [1, 2, 3 ,'a', 'b']

print('------')

a = [15 , 5 , 67 , 3 ]

print(max(a))     # 67
print(min(a))     # 3
print(sum(a))     # 90

print(a.count(5)) # 1

a.insert(2,8)
print(a)          # [15, 5, 8, 67, 3]

a.remove(67)
print(a)          # [15, 5, 8, 3]

print(a.pop())    # 3
print(a)          # [15, 5, 8]

print(a.pop(1))   # 5
print(a)          # [15, 8]

del a[1]
print(a)          # [15]

print('------')
a = [3,7,5,4]
a.reverse()
print(a)          # [4,5,7,3]

a.sort()
print(a)          # [3,4,5,7]

print('------')

a = [1,2]
a.append(9)
print(a)          # [1, 2, 9]

print('------')
x = [1, 2]
y = ['a','b']
x.append(y)
print(x)          # [1, 2, ['a','b']]
print(len(x))     # 3
print('------')

x = [1, 2]
y = ['a','b']
x.extend(y)
print(x)          # [1, 2,'a','b']
print(len(x))     # 4

print('------')

a = [1, 2, 3, 4]
a.clear()
print(a)          # []
print(len(a))     # 0

print('------')

a = [1,2]
b = a.copy()
print(b)         # [1, 2]

print('------')

a = []
for i in range(3):
    a.append(i)
    
print(a)          # [0, 1, 2]

# or
a = [i for i in range(3)]
print(a)          # [0, 1, 2]

print('------')

grade = [5, 18, 20, 4, 7]

a = [i for i in grade if i > 10]
print(a)                          # [18,20]

print('------')

###################################################################

"""
    Tuple:
    len , index, sum , min , max , count , ...
"""

t = ('English', 'Art', 'Mathematics')

print(type(t))   # <class 'tuple'>

print(len(t))    # 3

print(t[1])      # Art

print(t[1:3])    # ('Art', 'Mathematics')

print(t.index('Art'))      # 1

print( 'Art' in t)         # True

# t[0] = 'history'         # error : tuples are immutable

print('------')

t = (1, 7, 5) 
   
print(sum(t))      # 13
print(max(t))      # 7
print(min(t))      # 1

print(t.count(9))  # 0

print(tuple(reversed(t)))  # (7,5,1)

print('------')

t = (1, 2)
a = list(t)
a.append(3)
t = tuple(a)
print(t)           # (1, 2, 3)

print('------')

t = (14, 7, 3, 19)
x = list(t)
x.remove(3)
t = tuple(x)
print(t)          # (14, 7, 19)

print('------')

t = ('red', 8)
x,y = t
print(x)         # red
print(y)         # 8

print('------')

a = (1, 2)
b = ('x', 'y')

c = zip(a,b)

print(list(c))           # [(1, 'x'), (2, 'y')]

# unzip
x = [(1, 'x'), (2, 'y')]
u = zip(*x)
print(list(u))          # [(1, 2), ('x','y')]

print('------')

###################################################################

"""
   dictionary:
       len , get , keys , values , items , pop , popitems ,... 
"""
print('# dict #')
      
      
d = {
     'brand' : 'b' , 
     'model' : 'm' ,
     'color' : 'red' , 
     'year'  : 2020
     }

# or 
# d = dict( brand = 'b' , model='m' , color = 'white' , 'year' = 2020)


print('------')

d = {'x': 14, 'y': 32, 'z': 11, 'w': 7}

print(type(d))           # <class dict>

print(len(d))            # 4

print( d['y'])           # 32

print(d.get('y'))        # 32

print(list(d.keys()))    # ['x', 'y', 'z', 'w']

print(list(d.values()))  # [14, 32, 11, 7]

print(list(d.items()))   # [('x', 14), ('y', 32), ('z', 11), ('w', 7)]

for k,v in d.items():
    print(k,':',v)
'''
x : 14
y : 32
z : 11
w : 7
'''    

d.pop('y')    
print(d)                 # {'x': 14, 'z': 11, 'w': 7}

d.popitem()
print(d)                 # {'x': 14, 'z': 11}

d.clear()
print(d)                 # {}

del d

print('------')

d = {'x': 14, 'y': 32, 'z': 11, 'w': 7}

import operator

k = operator.itemgetter(1)

print(sorted(d.items(),key = k))

# [('w', 7), ('z', 11), ('x', 14), ('y', 32)]

print('------')

# combine
d1 = {'x' : 3 , 'y': 2 , 'z':1}
d2 = {'w' : 8 , 't': 7 }
d = {}

d = d1.copy()
d.update(d2)

print(d)      # {'x': 3, 'y': 2, 'z': 1, 'w': 8, 't': 7}

# or
d = {**d1 , **d2} 

print('------')

k = ['a' , 'b'] 
v = [4 , 8]

z = zip(k,v)

d = dict(z)     
print(d)       # {'a': 4, 'b': 8}

print('------')

### Nested dict

myfamily = {
        'child1': {'name':'taha'  , 'age' : 8}  ,      
        'child2': {'name':'mahsa' , 'age' : 20}              
        }

print('------')

p = {
     'name'     : 'farshid', 
     'children' : ['mahsa', 'taha'],
     'phone'    : {'home':'021-4455', 'mobile':'0912-1972028'}
    }

print(len(p))                # 3

print(p['phone']['mobile'])  # 0912-1972028

print(p['children'][0])      # mahsa

###################################################################

"""
    Set :
        len , add, update , remove , discard , pop , copy , clear,
        intersection , union , difference , update , issubset , isdisjoint , ...
"""

S = {'a','e','o','i'}

print(type(S))     # <class 'set'>

print(len(S))      # 4

print('u' in S)    # False

S.add('u')
print(S)           # {'i', 'u', 'e', 'a', 'o'}

print('------')

S.remove('i')
print(S)           # {'u', 'e', 'a', 'o'}

print('------')

c = S.copy()
print(c)          # {'a', 'o', 'e', 'u'}

print('------')

S.clear()
print(S)                   # set()
print(len(S))              # 0

print('------')

X = {1, 2, 3 ,4 , 5}
Y = {2, 4}

print(X.intersection(Y))    # {2, 4}
print(X & Y)                # {2, 4}

print('------')

print(X.union(Y))           # {1, 2, 3, 4 , 5}
print(X | Y)                # {1, 2, 3, 4 , 5}

print('------')

print(X.difference(Y))      # {1, 3, 5}
print(X-Y)                  # {1, 3, 5}

print('------')

X = {'A', 'M'}
Y = {'A','C','M','F'}
print(X.issubset(Y))       # True


###########################################################
print('function')
###########################################################

def f():
    print('shirafkan')
    
f() 
#
def g():
    return 'shirafkan'

print(g())
#
def h(p):
    print(p)

h('shirafkan')    

print('------')

def f(x,y):
    if x > y :
        return x
    return y

def g(x,y,z):
    return f(x , f(y,z))

print(g(3,8,2))  # 8

print('-------------')

x = 7
def func():
    global x
    print(x)   # 7
    x = 3
    print(x)   # 3
    
func()    
print(x)       # 3

print('-------------')

def f(a, b):
    a *= 2
    b += 3
    return a, b

x = 4
y = 6
m, n = f(x, y)
print(m)        # 8
print(n)        # 9

print('-------------')

def f(lst):
    lst[0] *= 2
    lst[1] /= 3
    
a = [4, 9] 
f(a)  
print(a[0])    # 8
print(a[1])    # 3.0

print('-------------')

def h(my_dict):
    my_dict['x'] *= 2
    my_dict['y'] /= 3
        
d = {'x':4  , 'y':9}    
h(d)
print(d['x'])    # 8
print(d['y'])    # 3.0

print('-------------')

def test(x, y):
    print(x, y)

test(5, 2)           # 5 2
test(x = 5 , y = 2)  # 5 2
test(y = 2 , x = 5)  # 5 2
test(5 , y = 2)      # 5 2

print('-------------')

# keyword only argument

def f(*, x=8):
    print(x)
    
f()        # 8
f(x = 2)   # 2
#f(3)     #  f() takes 0 positional arguments but 1 was given

print('-------------')
# var arguments

def add_more(a, b, *c):
    print(a + b + sum(c))

add_more(5, 2, 7 , 8 , 12)   # 5+2+7+8+12=  
add_more(2, 6)               # 8

print('-------------')

def f(*x , y='.'):
    return y.join(x)

print(f('ali', 'reza'))                     # ali.reza
print(f('ali', 'reza', 'sara', y='/'))      # ali/reza/sara

print('-------------')

def test(a ,*, b=7, c=9):
    print(a,b,c)
    
test(5)         # 5  7  9
test(1, b=4)    # 1  4  9

# test(1, b=2, 6)    #  positional argument follows keyword argument

# test(1, 3, c=4) 
'''
test() takes 1 positional argument but 2 positional arguments 
(and 1 keyword-only argument) were given
'''
    
print('-------------')

def f(a, b , *c , **d):
    print(a)  # 3
    print(b)  # 4
    print(c)  # (7, 1, 6)
    print(d)  # {'x': 5, 'y': 7, 'z': 9}

f(3, 4, 7, 1, 6, x=5, y=7, z=9)    


print('-------------')

def count_char(s):
    d = {}
    for i in s:
        if i in d.keys():
            d[i] +=1
        else:
            d[i] = 1
    return d

print(count_char('abbcfab'))       # {'a': 2, 'b': 3, 'c': 1, 'f': 1}  


print('-------------')

'''
switch(a){
   case 1: return 'one' ;break;
   case 2: return 'two' ;break;
   defualt :return 'nothing';
}
'''

def switch(a):
    d = {1:'one' , 2 : 'two'}
    return d.get(a,'nothing')

print(switch(1))  # one
print(switch(2))  # two
print(switch(3))  # nothing
   
print('-------------')
a = [1, 2, 3, 1, 4, 2]

def unique_list(lst):
    r = []
    for i in lst:
        if i not in r:
            r.append(i)
    return r            

print(unique_list(a))              # [1, 2, 3, 4]
    
print('-------------')

def unique_list_2(lst):
   return list(set(lst))

print(unique_list_2(a))            # [1, 2, 3, 4]

print('--- PEP 484 --------')

def greeting(name: str) -> str:
    return 'Hello ' + name

print(greeting('farshid'))         # Hello farshid

print('-----------')

def add(x:int, y:int) -> int:
    '''
     sum two number
    '''
    print(x+y)

add(2, 3)  # 5
   
print(add.__annotations__)
# {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}

print(add.__doc__)   # sum two number

   
###############################################################
print('recursive')
##############################################################
'''
iterative:
            n! = 1*2*3*...*n
            
recursive:
            n! = n * (n-1)!
            1! = 1

4! = 4 * 3! = 4 * 6 = 24
3! = 3 * 2! = 3 * 2 = 6
2! = 2 * 1! = 2 * 1 = 2
1! = 1

'''

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(4))     # 24

print('---------------')


def f(n,base):
     s = '0123456789ABCDEF'
     if n < base:
         return s[n]
     else:
         return f(n//base , base) + s[ n % base]

print(f(25,16))       # 19

'''
f(25,16) = f(1,16) + s[9] = 1 + 9 = 19
f(1,16)  = s[1]  = 1

'''

print(f(8,2))         # 1000


print('-------------')

def binary_search(lst, x, start=0, end=None):
    if end is None:
        end = len(lst) - 1
    if start > end:
        return False
    mid = (start + end) // 2
    if x == lst[mid]:
        return mid
    if x < lst[mid]:
        return binary_search(lst, x, start, mid - 1)
    return binary_search(lst, x, mid + 1, end)

a = [2, 4, 7, 12, 19, 25, 38]
print(binary_search(a, 19 ))    # 4
print(binary_search(a, 4 ))     # 1
print(binary_search(a, 20))     # False


###############################################################
print('lambda')
##############################################################

add = lambda x, y : x * y 
print(add(2, 3))   # 6

print('-------------')

f = lambda x, y : (x + y , x - y)
print(f(8, 1))                     # (9, 7)

print('---map---')

lst = ['ALI', 'REZA'] 
print(list(map(str.lower, lst)))     #['ali', 'reza']

print('-------------')

a = ['mahsa', 'sara']
b = [20, 16]

print(list(zip(a,b)))                # [('mahsa', 20), ('sara', 16)]

print(list(map(lambda x, y : (x,y) , a , b))) 

print('-------------')

a = [1, 3]
b = [2, 4]
print(list(map(lambda x, y :x+y, a, b)))   # [3, 7]

print('-------------')

a = [16, 7, 14, 6]
print(list(map(lambda x : x < 10 , a)))    # [False, True, False, True]

print('--- filter ---')

a = [16, 7, 14, 6]
print(list(filter(lambda x : x < 10 , a)))  # [7, 6]

print('-------------')

a = [12, 17, '', 6,'' , 18]
print(list(filter(None,a)))       # [12, 17, 6, 18]

print('--- reduce ---')

from functools import reduce

lis = [12, 17, 6, 18]
add = lambda a,b : a+b

print(reduce(add, lis))        # 53   : (((12+17)+6)+18)


print('----- sorted --------')

lst = [12, 17, 6, 18]
print(sorted(lst))             # [6, 12, 17, 18]

print('-------------')

d = {'ali' : 12, 'sara' : 17, 'taha' : 6 , 'mahsa' : 18}
print(sorted(d.items() , key = lambda x : x[1]))

# [('taha', 6), ('ali', 12), ('sara', 17), ('mahsa', 18)]



































































































