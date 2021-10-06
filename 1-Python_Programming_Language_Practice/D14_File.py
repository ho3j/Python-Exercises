'''
Text 

Binary 
'''

f = open('d:/myfile.txt','w')
line1 = 'Hello Python\n'
line2 = 'C++\n'
line3 = str(52)
f.write(line1)
f.write(line2)
f.write(line3)
print(f.name)   # d:/myfile.txt
print(f.mode)   # w

f.close()

print('----')

with open('d:/myfile2.txt','w') as myfile:
    line1 = 'Hello Python\n'
    line2 = 'C++\n'
    myfile.write(line1)
    myfile.write(line2)

print('----')

#
#try :
#    f = open('d:/myfile.txt','r')
#except FileNotFoundError :
#    print('error')

print('----')

with open('d:/myfile2.txt','r') as f:
    data = f.readlines()
    print(data)            # ['Hello Python\n', 'C++\n']
    
    
print('----')

with open('d:/myfile2.txt','r') as f:
    print(f.readline())               # Hello Python
        
    
print('----')

with open('d:/myfile2.txt','r') as f:
     print(f.read(3))                  # Hel
     print(f.read(5))                  # lo Py
    
print('----')

with open('d:/myfile2.txt','r') as f:
    for line in f:
        print(line, end='')
    
    
print('----')

with open('d:/myfile2.txt','r') as f:
     x = f.read()
     print(x)    
    
    
print('----')

import os
n = 'd:/myfile2.txt'
print(os.path.exists(n))  # True
os.remove(n)


print('----')

name1 = 'd:/myfile.txt'
name2 = 'd:/a.txt'

with open(name1,'r') as f1 , open(name2, 'w') as f2:
    for line in f1:
        f2.write(line)


print('----')

name1 = 'd:/x.txt'
name2 = 'd:/y.txt'
name3 = 'd:/z.txt'

with open(name1, 'w') as f1:
    f1.write('ali\n')
    f1.write('sara\n')
    
with open(name2, 'w') as f2:
    f2.write('taha\n')
    f2.write('omid\n')
    f2.write('mahsa\n')
    
with open(name1) as f1 , open(name2) as f2:
      data1 = f1.read()
      data2 = f2.read()

with open(name3,'w')  as f3:
    f3.write(data1 + data2)
        

print('----')

lst = ['yes','no','no','yes','yes','yes','no']

name = 'd:/answer.txt'

with open(name, 'w') as f:
    for i in lst:
        f.write(i)
        f.write('\n')

c1 = 0
c2 = 0

with open(name, 'r')  as f:
     lst = f.readlines()       
     for i in lst:
         x = i.strip()
         if x == 'yes':
            c1 += 1
         else :
            c2 += 1
print(c1)   # 4         
print(c2)   # 3


d = dict()
with open(name) as f:
    for line in f:
        w = line.split()
        for i in w:
            d[i] = d.get(i, 0) + 1
print(d)                            # {'yes': 4, 'no': 3}           


print('----')

def count(filename):
    try:
        with open(filename) as f:
            x = f.read()
    except FileNotFoundError as e:
        print(e)        
    else:    
        c = len(x.split())
        print(f'{filename} : {c}')
        

count('d:/x.txt')         # d:/x.txt : 2
count('d:/h.txt')         # No such file or directory:
count('d:/answer.txt')    # d:/answer.txt : 7 


print('----')

def count(filename):
    try:
        with open(filename) as f:
            x = f.read()
    except FileNotFoundError as e:
        print(e)        
    else:    
        c = len(x.split())
        print(f'{filename} : {c}')
        
lst = ['d:/x.txt' , 'd:/h.txt' ,'d:/answer.txt' ]
for i in lst:
    count(i)
 
    
print('-----')

with open('d:/test.txt' , 'w') as myfile:
    myfile.write('ABCDEF')

with open('d:/test.txt', 'r')  as f:
    print(f.tell())   # 0
    print(f.read(1))  # A
    f.seek(3)
    print(f.read(2))  # DE
    print(f.tell())   # 5
    print(f.read(1))  # F

print('-----')

with open('d:/test.txt','rb' )  as f:
    print(f.tell())   # 0
    print(f.read(1))  # b 'A'
    f.seek(3)
    print(f.read(2))  # b 'DE'
    print(f.tell())   # 5
    print(f.read(1))  # b 'F'
    f.seek(-5,2)
    print(f.read(1))  # b'B'

print('-----')

line1 = 'ali\n'
line2 = 'sara\n'
lst = [line1, line2]

with open('d:/g.txt' , 'w') as f:
    f.writelines(lst)


print('-----')

line3 = 'mahsa'

with open('d:/g.txt' , 'a') as f:
     f.write(line3)
     
     
print('-----')

x = b'farshid'
print(x)            # b'farshid'
print(x.decode())   # farshid

b = bytes([65, 97])
print(b)               # b'Aa'
print(b.decode())      # Aa


a = bytearray([65, 97])
print(a)               # bytearray(b'Aa')
print(a.decode())      # Aa

print('-----')

data = 'Hello\nPython'
print(data)

b = bytes(data, 'utf-8')
print(b)                  # b'Hello\nPython'

with open('d:/myfilebin.bin', 'wb')  as f:
    print(f.write(b))                         # 12


print('-----')

import json

d = {'k1':'v1' , 'k2':'v2'}

js = json.dumps(d)
print(js)          # {"k1": "v1", "k2": "v2"}

print(json.dumps(d , indent = 4))
'''
{
    "k1": "v1",
    "k2": "v2"
}
'''
print(json.dumps(d , indent = 4 , separators = (';','=')))
'''
{
    "k1"="v1";
    "k2"="v2"
}
'''

with open('d:/j.json', 'w') as f:
    json.dump(d, f)
    
with open('d:/j.json') as f:
    print(json.load(f))      # {'k1': 'v1', 'k2': 'v2'}
    

print('-----')

import pickle 

with open('d:/p.bin', 'wb') as f:
    pickle.dump(d, f)
    
with open('d:/p.bin','rb') as f:
    print(pickle.load(f))    
    
print('-----')

import csv
x  = ['Name' , 'Age'] 
r1 = ['ali',35]
r2 = ['taha',10]
r3 = ['mahsa',40]

with open('d:/a.csv','w') as f:
    w = csv.writer(f)
    w.writerow(x)
    w.writerows([r1,r2,r3])
    
    
with open('d:/a.csv', newline = '\n') as f:
    r = csv.reader(f)
    for i in r:
        print('   '.join(i))
'''
Name   Age
ali   35
taha   10
mahsa   40
'''

print('-----')

import pandas as pd

data = pd.read_csv('d:/a.csv')
print(data)

data.to_csv('d:/b.csv',sep=',', index = False)

print('-----')

import glob
print(glob.glob('d:/a*.csv'))




















