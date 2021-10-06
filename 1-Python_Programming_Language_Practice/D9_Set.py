"""
    Set
"""

f = {'apple', 'orange' , 'banana'}

print(type(f))  # <class 'set'>

print(len(f))  # 3

print(f)       # {'orange', 'banana', 'apple'}

for i in f:
    print(i)
                #banana
                #orange
                #apple

f1 = set(('apple', 'orange' , 'banana'))    

print(f == f1)   # True

print('cherry' in f)   # False

f.add('cherry')
print(f)       # {'orange', 'banana', 'cherry', 'apple'}

f.update(['mango' , 'grapes'])
print(f)   
# {'cherry', 'orange', 'banana', 'apple', 'mango', 'grapes'}

f.remove('apple')
print(f) 
# {'cherry', 'orange', 'banana', 'mango', 'grapes'}

###
vowels = {'a','e','o','i','u'}
print(vowels)  # {'e', 'i', 'u', 'o', 'a'}

# vowels.remove('k')  # KeyError: 'k'

vowels.discard('h')  # Not raise an error

x = vowels.pop()
print(x)         # e
print(vowels)    # {'i', 'u', 'o', 'a'}


c = vowels.copy()
print(c)

vowels.clear()
print(vowels)   # set()
print(len(vowels))  # 0

del c


####
# difference

A = {1,2,3,4,5}
B = {2,4,7}

print(A-B)   # {1,3,5}
print(B-A)   # {7}

r = A.difference(B)
print(r)   # {1, 3, 5}
print(A)   # {1, 2, 3, 4, 5}
print(B)   # {2, 4, 7}


r = A.difference_update(B)
print(r)   # None
print(A)   # {1, 3, 5}
print(B)   # {2, 4, 7}


X = {1, 2, 3}
Y = {2 ,3, 4}
print(X.symmetric_difference(Y))  # {1, 4}
print(X ^ Y)                      # {1, 4}

X = {1, 2, 3}
Y = {2 ,3, 4}
print(X.intersection(Y))    # {2, 3}
print(X & Y)                # {2, 3}

X = {1, 2, 3}
Y = {2 ,3, 4}
print(X.union(Y))   # {1, 2, 3, 4}
print(X | Y)        # {1, 2, 3, 4}

X = {1, 2, 3}
Y = {2 ,3, 4}
X.update(Y)
print(X)             # {1,2,3,4}

X = {56 , 98}
s ='ali'
a = [13,25]
t = (7 , 8 )
d = {'one':1 , 'two':2}

X.update(s,a,t,d)
print(X) # {'two', 98, 7, 8, 'i', 13, 'one', 'l', 56, 25, 'a'}


######
# isdisjoint

X = {1, 2}
Y = {1, 2, 3}
print(X.isdisjoint(Y))   # False

X = {1, 2}
Y = {3, 7, 8}
print(X.isdisjoint(Y))   # True

####

X = {1, 2}
Y = {1, 2 , 3}
print(X.issubset(Y))  # True
print(Y.issubset(X))  # False

###
w = 'alireza'
x = {'a' , 'r'}
s = set(w)
print(x.intersection(s))  # {'a', 'r'}

###
# match
d1 = {'a':1 , 'b':3 , 'c':2}
d2 = {'a':2 , 'b':3 , 'c':1}

s1 = set(d1.items())
s2 = set(d2.items())
s = s1 & s2

for k,v in s:
    print(k)    # b
    
###
s1 = 'abcd'

s2 = 'bxd'    
# acx
















































