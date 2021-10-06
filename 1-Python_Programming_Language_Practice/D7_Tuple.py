"""
    Tuple
"""
t = ('English', 'History', 'Mathematics')
print(t)
print(type(t))   # <class 'tuple'>
print(len(t))    # 3

print(t[0])      # English
print(t[1:3])    # ('History', 'Mathematics')

print(t.index('English'))  # 0
print( 'English' in t)     # True

# t[0] = 'art'  # error : tuples are immutable

for i in t:
    print(f'I like to read {i}')
'''
I like to read English
I like to read History
I like to read Mathematics
'''

t = (1, 9 , 2)    
print(sum(t))      # 12
print(max(t))      # 9
print(min(t))      # 1
print(t.count(9))  # 1
print(t*2)         # (1, 9, 2, 1, 9, 2)

print(reversed(t))  # <reversed object at 0x00000243923BE6A0>
print(tuple(reversed(t)))  # (2, 9, 1)

t = (3,)

s = ('a',)

t1 = (1,2)
t2 = (2,1)
print(t1 == t2)   # False



# append ?
t = (4 , 6)
t = t + (9,)
print(t)     # (4, 6, 9)

# or
t = (4 ,6)
a = list(t)
a.append(9)
t = tuple(a)
print(t)    # (4, 6, 9)


# remove ?
t = (4, 7, 2, 9, 8)
x = list(t)
x.remove(2)
t = tuple(x)
print(t)     # (4, 7, 9, 8)
###############################################
# unpack
t = (4, 8)
a,b = t
print(a)   # 4
print(b)   # 8

car = ('blue', 'auto', 7)
color,_,a = car
print(color)    # blue
print(_)        # auto
print(a)        # 7

###############################################
# zip

a = (1, 2)
b = (3, 4)
c = zip(a,b)
x = list(c)
print(x)           # [(1, 3), (2, 4)]
print(x[0])        # (1,3)
print(type(x[0]))  # <class 'tuple'>

# unzip
z = [(1, 3), (2, 4)]
u = zip(*z)
print(u)    # <zip object at 0x00000233A39A90C0>
print(list(u))    # [(1, 2), (3, 4)]


a = (1, 2 , 'A')
b = (3, 4 , 8)
c = zip(a,b)
x = list(c)
print(c)        # <zip object at 0x000001FC04755180>
print(x)        # [(1, 3), (2, 4), ('A', 8)]

###############################################

num = [8, 2 , (9,3) , 4 , (1,6,7) , 34]
c = 0
for i in num:
    if isinstance(i , tuple):
        continue
    c += 1
print(c)              # 4
print(len(num) - c)   # 2

###############################################

a = [(1,2,3) , (4,5,6)]

b = [i[:-1]+(9,) for i in a]

print(b)   # [(1, 2, 9), (4, 5, 9)]

 







    





