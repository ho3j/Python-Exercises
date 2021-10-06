"""
   dictionary
   
   {"key" : "value"}
"""
d = {
     'brand' : 'cherry' , 
     'model' : 'arizo5' ,
     'color' : 'white'
     }

print(type(d))    # <class dict>

print(len(d))     # 3

d1 = dict( brand = 'cherry' , model='arizo5' , color = 'white')

d['year'] = '2010'

print(d) #{'brand': 'cherry', 'model': 'arizo5', 'color': 'white', 'year': '2010'}

print( d['model'])  # arizo5

x = d.get('model')
print(x)           # arizo5

x = d.get('cylinder')
print(x)           # None

x = d.get('cylinder',-1)
print(x)           # -1

print(d.keys())   #dict_keys(['brand', 'model', 'color', 'year'])
print(list(d.keys()))    # ['brand', 'model', 'color', 'year']

print(list(d.values()))  # ['cherry', 'arizo5', 'white', '2010']

print(list(d.items()))  
#[('brand', 'cherry'), ('model', 'arizo5'), ('color', 'white'), ('year', '2010')]

print()

for k,v in d.items():
    print(k,':',v)
    
                    #brand : cherry
                    #model : arizo5
                    #color : white
                    #year : 2010

d.pop('model')    
print(d)     # {'brand': 'cherry', 'color': 'white', 'year': '2010'}

d.popitem()
print(d)     # {'brand': 'cherry', 'color': 'white'}


d.popitem()
print(d)     # {'brand': 'cherry'}

d.clear()
print(d)    # {}

del d

#############
a = ['x', 'y', 'x', 'z', 'y', 'x']
d = {}

for i in a :
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1         
print(d)           # {'x': 3, 'y': 2, 'z': 1}

# or
d1 = {}
for i in a:
    d1[i] = d1.get(i,0) +1
    
print(d1)    

d2 = d.copy()



s = 'abfabdcaa'
d = {}
for i in s:
    d[i] = d.get(i,0) + 1
    
print(d)  #{'a': 4, 'b': 2, 'f': 1, 'd': 1, 'c': 1}


line ='a dictionary is a datastructure.'
d = {}
s = line.split()
print(s)  # ['a', 'dictionary', 'is', 'a', 'datastructure.']

for i in s:
    d[i] = d.get(i,0) + 1

print(d)
# {'a': 2, 'dictionary': 1, 'is': 1, 'datastructure.': 1}



d = {'a': 4, 'b': 2, 'f': 1, 'd': 1, 'c': 1}

s = 0
for i in d:
    s += d[i]
print(s)       # 9

# or
print(sum(d.values()))  # 9


print('# sort #')
d = {'a': 4, 'b': 2, 'f': 1, 'd': 1, 'c': 1}
import operator
k= operator.itemgetter(1)
print(sorted(d.items(),key = k))
# [('f', 1), ('d', 1), ('c', 1), ('b', 2), ('a', 4)]

k= operator.itemgetter(0)
print(sorted(d.items(),key = k))
# [('a', 4), ('b', 2), ('c', 1), ('d', 1), ('f', 1)]

####

num ={
      'ali' : [12,13,8],
      'sara': [15,7,14],
      'taha': [5,18,13]     
      }

d = {k : sorted(v)  for k,v in num.items()}

print(d)

# {'ali': [8, 12, 13], 'sara': [7, 14, 15], 'taha': [5, 13, 18]}

###

# combine

d1 = {'x' : 3 , 'y': 2 , 'z':1}
d2 = {'w' : 8 , 't': 7 }

d = {}
d = d1.copy()
d.update(d2)
print(d)
# {'x': 3, 'y': 2, 'z': 1, 'w': 8, 't': 7}

# or
d = {}
for i in (d1,d2):
    d.update(i)
print(d)   

# or
d = {**d1 , **d2} 
print(d)

####
# Map two lists into a dict
k = ['red' , 'green'] 
v = ['#FF0000' , '#008000']

z = zip(k,v)
d = dict(z)     

print(d)   # {'red': '#FF0000', 'green': '#008000'}

###

s = 'alireza'
x = ['a', 'r']
d = {}

for i in s:
    if i in x:
        d.setdefault(i,0)
        d[i] +=1

print(d)         # {'a': 2, 'r': 1}

###
# remove duplications
d = {'x': 3, 'y': 2, 'z': 1, 'y' :2 , 'z' : 4 }

r = {}

for k,v in d.items():
    if v not in r.values():
        r[k] = v

print(r)         # {'x': 3, 'y': 2, 'z': 4}


###
d = {
     'h' : 0 , 
     't' : 0
     }

import random

for i in range(17):
    d[random.choice(list(d.keys()))] +=1

print(d)    #{'h': 10, 't': 7}

###

students = [ 
             {'id':123 , 'name' : 'ali'  , 's': True},
             {'id':378 , 'name' : 'taha' , 's': False},
             {'id':934 , 'name' : 'sara' , 's': True} 
            ]

print(sum(d['s']  for d in students))   #2

print(students[1])  # {'id': 378, 'name': 'taha', 's': False}

### Nested dict

myfamily = {
        'child1':{'name':'taha'  , 'age' : 8}  ,      
        'child2':{'name':'mahsa' , 'age' : 20}              
        }

print(myfamily)

# or
d1 = {'name':'taha'  , 'age' : 8} 
d2 = {'name':'mahsa' , 'age' : 20}

myfamily1 = {
        'child1':d1 ,      
        'child2':d2              
        }

###
tel = {
       'home' : '021-4455' , 
       'mobile' : '0912-1972028'
       }

person ={
         'name'     : 'farshid' , 
         'age'      : 48 , 
         'children' : ['mahsa' , 'taha'],
         'phone'    : tel
        }

print(len(person))  # 4

print(person['phone']) # {'home': '021-4455', 'mobile': '0912-1972028'}

print(person['phone']['mobile']) #0912-1972028

print(person['children'])     # ['mahsa', 'taha']
print(person['children'][0])  # mahsa

print(person.pop('age'))








