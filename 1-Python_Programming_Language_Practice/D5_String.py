s = 'abcde'
print(s[1:3])   # bc
print(s[1:-1])  # bcd
print(s[1:4])   # bcd

print(s[::-1])  # edcba

s = 'shirafkan'
print(len(s))   # 9 
print(max(s))   # s
print(min(s))   # a

print(ord('A')) # 65
print(ord('a')) # 97

print(chr(97))  # a

s = 'python'
print( 'th' in s)       # True
print( 'xh' not in s)   # True

print( s == 'python')   # True

print( s < 'sara')      # True

print(s.islower())      #True
print(s.isupper())      #False

print(s.isalnum())      #True
print(s.isalpha())      #True

s = 'python3'
print(s.isalnum())     # True
print(s.isalpha())     # False

s = '#python3'
print(s.isalnum())     # False
print(s.isalpha())     # False

s = '123'
print(s.isdigit())     # True

print('\t'.isspace())   #True

print('\n===============================')

s = '12a3bcd4'
k = 0
for ch in s:
    if (ch.isdigit() == True ):
        k += int(ch)

print(k)         # 10 : 1+2+3+4

print('\n===============================')

s = 'welcom to python'
print(s.startswith('we'))   # True
print(s.endswith('thon'))   # True

print(s.find('o'))           # 4
print(s.index('o'))          # 4 first index of left

print(s.find('f'))           # -1
#print(s.index('f'))          # ValueError


print(s.find('o',5))        # 8   start 5 to end
print(s.find('o',10))       # 14

print(s.count('o'))         # 3
print(s.count('o',5))       # 2

s = 'farshid@ut.ac.ir'
i = s.find ('@')
print(s[i+1:])              # ut.ac.ir



s = 'welcom to python'
print(s.capitalize())     # Welcom to python
print(s.title())          # Welcom To Python

s = 'PyThon'
print(s.lower())         # python
print(s.upper())         # PYTHON
print(s.swapcase())      # pYtHON

s = 'shirafkan'
print(s.replace('afkan','del'))   # shirdel

s = '$$pyt$hon$$$'
print(s.strip('$'))     # pyt$hon
print(s.lstrip('$'))    # pyt$hon$$$
print(s.rstrip('$'))    # $$pyt$hon

s = '##ali$$$'
print(s.lstrip('#').rstrip('$'))  # ali
               
s = 'www.sanjesh.org'
print(s.lstrip('www.'))  # sanjesh.org

s = 'Python created by Rossum'
a = s.split(' ')    #--> list
print(a)            # ['Python', 'created', 'by', 'Rossum']

b = ['Python', 'created', 'by', 'Rossum']
c =' '.join(b)       #Python created by Rossum
print(c)

name = 'ali.py'
a = name.split('.')
print(a)           # ['ali', 'py']
print(a[1])        # py
print(repr(a[1]))  # 'py'

s = 'sara@gmail.com'
u ,d = s.split('@')
print(u)   # sara
print(d)   # gmail.com

s = 'ali\nreza'
a = s.split('\n')
print(a)           # ['ali', 'reza']

b = s.splitlines()
print(b)           # ['ali', 'reza']

s = '127.02.0.001'
b = s.split('.')
a = '.'.join([str(int(i)) for i in b])
print(a)   # 127.2.0.1

f = '001'
print(int(f))       # 1
print(str(int(f)))  # 1

s = '12'
print(s.zfill(5))   # 00012
print(s.zfill(3))   # 012

s = 'sara'
print(s.ljust(7,'+'))      # sara+++
print(s.rjust(7,'+'))      # +++sara
print(s.center(7,'+'))     # ++sara+

year = 2020
e   = 'referendum'
print(f'Results of the {year} {e}') # Results of the 2020 referendum

#############################################

print('# format #')
fname = 'sara'
lname = 'shirafkan'
print('name:{0} family:{1}'.format(fname,lname)) # name:sara family:shirafkan

print('name:{1} family:{0}'.format(fname,lname)) # name:shirafkan family:sara
print('name:{0} family:{0}'.format(fname,lname)) # name:sara family:sara



s = 'ali'
print(f'name : {s}')     # name : ali
print(f'name : {s!r}')   # name : 'ali'

print('name:{}'.format(s))     # name:ali
print('name:{!r}'.format(s))   # name:'ali'


n = 14
print('{:d}'.format(n))   #14     {index format : type }
print('{0:d}'.format(n))  #14

print('{:5d}'.format(n))  #   14
print('{:9d}'.format(n))  #       14

a = 12
b = 15
print('{0:f} {1:d}'.format(a,b))   # 12.000000  15
print('{1:f} {0:d}'.format(a,b))   # 15.000000  12
print('{0:d} {1:f}'.format(a,b))   # 12 15.000000

f = 15.999
print('{:.2f}'.format(f))   # 16.00
print('{:10.2f}'.format(f))   #     16.00

f = 15.99999999
print('{:.2f}'.format(f))   # 16.00
print('{:15.2f}'.format(f))   #           16.00
print(f'name : {f}')          #15.99999999
print('{0:.2f}'.format(f))  # 16.00
print('{:.6f}'.format(f))   # 16.000000

f = -15.999
print('{:.2f}'.format(f))   # -16.00

p = 0.83
print('{:.2%}'.format(p))  # 83.00%
print('{:.5%}'.format(p))  # 83.00000%

a = 20000000
print('{:,}'.format(a))     # 20,000,000

n = 14
print('{:X}'.format(n))     # E  
print('{:#X}'.format(n))    # 0XE  

print('{:b}'.format(n))     # 1110       
print('{:#b}'.format(n))     # 0b1110      
    
n = 35
print('{:*>6d}'.format(n))    # ****35
print('{:*<6d}'.format(n))    # 35****
print('{:*^6d}'.format(n))    # **35**










