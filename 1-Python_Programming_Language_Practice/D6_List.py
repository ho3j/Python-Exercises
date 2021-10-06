"""
    list
    'index' ,'count','insert','remove','pop','reverse'
    , 'sort' ,'extend', 'append','clear','copy',
    
"""
a = [5 , 7, 12]
print(type(a))    # <class 'list'>
print(len(a))     # 3

print(a.index(7))   # 1
print(a[1])         # 7
a[1] = 8            # list is mutable

s = 'sara'
print(s[1])
# s[1]='d'         # string is immutable

a = [1, 2]
b = [2, 1]
print(a == b)    # False because (list is ordered)

friends = ['ali','sara','taha']
for f in friends:
    print(f)
                                    #ali
                                    #sara
                                    #taha
for i in range(3):
    print(friends[i])

                                    #ali
                                    #sara
                                    #taha
                                    
L = [3,6,True , 'ali',2.7 , [5,8]]  


a = [7, 5, 30, 2, 6, 25]
print(a[1:4])        # [5 ,30 , 2]
print(a[:3])         # [7 , 5 , 30]
print(a[3:])         # [2 , 6 , 25]
print(a[3:0])        # []

print(a[::-1])       # [25, 6, 2, 30, 5, 7]

print(a[0:7:2])      # [7, 30, 6]
print(a[6:0:-2])     # [25, 2, 5]

a[3:5]=[14, 15]
print(a)            # [7, 5, 30, 14, 15, 25]

a = [4, 7]
b = a*2
print(b)           # [4, 7, 4, 7]

a = [1, 2]
b = ['a', 'b', 'c']
c = a + b
print(c)           # [1, 2, 'a', 'b', 'c']


a = [7, 5, 30, 2, 6, 25]
print( 14 in a)     # False
print(14 not in a)  # True

a = [3, [109, 27], 4, 15] 
print( 27 in a)     # False

print(a[1])     # [109, 27]
print(a[1][1])  # 27 
print(len(a))   # 4


###################################

a = [7 , 5 , 30 , 2 , 6 , 25]
m = -1
for i in a:
    if i > m:
        m = i

print(m)          # 30

print(max(a))     # 30
print(min(a))     # 2
print(sum(a))     # 75

s = 0 
for i in a:
    s += i
print(s)         # 75


a = [1, 2, 6, 5, 2]
print(a.count(2))      # 2


a = [1, 2, 6, 5, 2]
a.insert(2,13)   #a.insert(index,value)
print(a)               # [1, 2, 13, 6, 5, 2]

a = [1, 2, 6, 5, 2]
a.remove(2)      #a.remove(value)
print(a)              #[1, 6, 5, 2]
a.remove(2)
print(a)              #[1, 6, 5]


x = [10, 15, 12, 8]
a = x.pop()          #output was
print(x)             # [10, 15, 12]
print(a)             # 8

y = ['a', 'b', 'c']
p = y.pop(1)
print(p)      # b
print(y)      # ['a','c']


a = [5 , 9 , 3]
del a[1]
print(a)      # [5, 3]


a = [0, 1, 2, 3, 4, 5, 6]
del a[2:4]
print(a)     #[0, 1, 4, 5, 6]

a = [1,2,3]
a.reverse()
print(a)        # [3, 2, 1]


a = [2,4,3,5,1]
a.sort()
print(a)       # [1, 2, 3, 4, 5]


x = [1, 2, 3]
y = [4, 5]
x.extend(y)
print(x)        # [1, 2, 3, 4, 5]
print(len(x))   # 5
print(len(y))   # 2


x = [1, 2, 3]
y = [4, 5]
y.extend(x)
print(y)        # [4, 5, 1, 2, 3]
print(len(x))   # 3
print(len(y))   # 5




x = [1, 2, 3]
y = [4, 5]
x.append(y)
print(x)        # [1, 2, 3,[4, 5]]
print(len(x))   # 4
print(len(y))   # 2

a = [1,2,3]
a.append(4)
print(a)      # [1, 2, 3, 4]


a = [1,2,3]
a.clear()
print(a)        # []
print(len(a))   # 0


a = [1,2,3]
b = a.copy()
print(b)      # [1, 2, 3]

##############################################

a = []
for i in range(4):
    a.append(i)
print(a)          # [0, 1, 2, 3]

a = [i for i in range(4)]
print(a)         # [0, 1, 2, 3]


a = [i*2 for i in range(4)]
print(a)         # [0, 2, 4, 6]

# [9, 16, 25]
a = [i*i for i in range(3,6)]
print(a)         # [9, 16, 25]

a = [1 , -2 , 5 , -56 , 8]
b = [abs(i) for i in a]
print(b)                       # [1, 2, 5, 56, 8]

import math
a = [round(math.pi,i) for i in range(1,5)]
print(a)       # [3.1, 3.14, 3.142, 3.1416]


a = ['$ali', 'sara$']
b = [i.strip('$') for i in a]
print(b)      # ['ali', 'sara']

a = [11, 8, 14, 20 , 2]
b = [i for i in a if i < 10]
print(b)   # [8, 2]

a = [1, 2]
b = [1 ,4, 5]
c = []
for i in a:
    for j in b:
        if i != j:
          c.append((i,j))
print(c)     # [(1, 4), (1, 5), (2, 1), (2, 4), (2, 5)]



a = [2.6, float('NaN') , 4.8 , 6.9, float('NaN')]
b = []
import math
for i in a:
    if not math.isnan(i):
        b.append(i)
print(b)                 # [2.6, 4.8, 6.9]


print('---- matrix ----')

m  = [
       [1,2,3],
       [4,5,6],
       [7,8,9]
      ]

print(len(m)) # 3

print(m[0])   # [1, 2, 3]   row

for i in m:
    print(i)

                                #[1, 2, 3]
                                #[4, 5, 6]
                                #[7, 8, 9]
                                
                                
for i in m:
    print(i[0],end=' ')   # 1  4  7 
                            #col
print()    

for i in range(0,3) :
    print(m[i][i],end=' ')  # 1  5  9
                            #ghotr asli
print()    

for i in range(0,3):
    print(m[i][2-i],end=' ') # 3  5  7
                            #ghotr farei
print()

a = []
a.extend([sum(i) for i in m])
print(a)    # [6, 15, 24] sum row

b = []
for col in range(3):
    b.append(sum(i[col] for i in m))
print(b)    # [12, 15, 18] sum col

    
print('-----')

x = 2
y = x
y += 1
print(x)   # 2
print(y)   # 3

x = []
y = x
y.append(5)
print(x)    # [5]
print(y)    # [5]

x = []
y = x.copy()
y.append(5)
print(x)    # []
print(y)    # [5]






