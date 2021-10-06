"""
Loop:
    
    for
    while
    
    
"""
for i in range(4):
    print(i)       
    
#0
#1
#2
#3
print('\n ==============')    

for i in range(4):
    print(i , end = ' ')      # 0 1 2 3 

print('\n ==============')    

for i in range(3,8):         #(start,end)   i khown withou end #8
    print(i , end= ' ')      # 3 4 5 6 7 
    
    
print('\n ==============')    

for j in range(5,10,2):     #(start,end,step)
    print(j , end = ' ' )   # 5 7 9 

print('\n ==============')    

s = 'farshid'
for ch in s:
    print(ch)
    
                            #f
                            #a
                            #r
                            #s
                            #h
                            #i
                            #d
print('\n ==============')    

s = 'farshid'
for ch in s:
    print(ch , end=' ')    #f a r s h i d 
    
print('\n ==============')    

for _ in range(3):
    print('hello')
                            #hello
                            #hello
                            #hello

print('\n ==============')   
 
for i in range(9,2,-3)    :
     print(i , end=' ' )     # 9 6 3 

print('\n ==============')    
     
word = 'python'    
c = 0 
for i in word:
    c+=1
print(c)                # 6

print('\n ==============')    

word = 'alireza'    
c = 0 
for i in word:
    if i =='a':
        c+=1
print(c)                # 2


print('\n ==============')    

name = 'farshid'
v = 'aeiou'
c = 0
for ch in name:
    if ch in v:
        print(ch)    # a i 
        c += 1
        
print(c)             # 2

print('\n ==============')    

name = 'farshid'
v = 'aeiou'
a = [ch for ch in name if ch in v]
print(a)            # ['a', 'i']

print('\n ==============')    

for i in range(1,4):             #row
    for j in range(2,4):         #col
        print(j,end=' ')
    print()
                                #2 3 
                                #2 3 
                                #2 3 
'''
i = 1  --> j=2 , j=3
i = 2  --> j=2 , j=3
i = 3  --> j=2 , j=3
'''
        
print('\n ==============')    

for i in range(1,4):
    for j in range(2,4):
        print(i,end=' ')
    print()
                                #1 1 
                                #2 2 
                                #3 3 

print('\n ==============')    

for i in range(4):
    for j in range(2,4):
        print(i,end=' ')
    print()
                                #0 0
                                #1 1
                                #2 2
                                #3 3
print('\n ==============')   
 

for i in range(2,5):
    for j in range(i):
        print(j,end=' ')
    print()
                                #0 1 
                                #0 1 2 
                                #0 1 2 3

'''
i = 2  : j=0 , j=1
i = 3  : j=0 , j=1 , j=2
i = 4  : j=0 , j=1 , j=2 , j=3
'''

print('\n ==============')    
'''
1
1  2
1  2  3
'''

for i in range(2,5):
    for j in range(1,i):
        print(j , end = ' ')
    print()        

    
print('\n # break #')    

for i in range(5):
    if i == 3 :
        break
    else:
        print(i,end=' ')   # 0 1 2 


print('\n # continue #')    

for i in range(5):
    if i == 3 :
        continue
    else:
        print(i,end=' ')   # 0 1 2 4

print('\n =======not prime =======')    
for n in range(2,20):
    for i in range(2,n):
        if n % i == 0 :
            print(n , end = ' ')   # 4 6 8 9 10 12 14 15 16 18
            break
        
print('\n ======prime========')    
for i in range(2,20):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i , end = ' ')   # 2 3 5 7 11 13 17 19
        



print('\n ==============')    

print('# while #')
      
i = 1      
while i<= 3:
    print(i , end= ' ')    # 1 2 3
    i += 1
print("\n i last : \t ",i)  # i last :         4

print('\n ==============')    

n = 7
while n >= 3:
    print(n , end = ' ')    # 7 6 5 4 3 
    n -= 1


print('\n ==============')    

s = 'abcdef'
i = 0
while True:
   if s[i] == 'd' :
       break
   print(s[i] , end= ' ')  # a b c
   i +=1
   
print('\n ==============')    

n = 8
while n > 2:
    n -= 1
    if n == 5:
        break
    print(n , end = ' ')    #7 6

    
print('\n ==============')    

n = 8
while n > 2:
    n -= 1
    if n == 5:
        continue
    print(n , end = ' ')    #7 6 4 3 2 
    
    
print('\n ==============')    
      
a = 0
b = 1
while a < 10:
    print(a,end=' ')   # 0 1 2 4 8
    a = b
    b = a+b
     
print('\n ==============')    
      
a = 0
b = 1
while a < 10:
    print(a,end=' ')   # 0  1  1  2  3  5  8
    a  , b = b , a+b

    
print('\n ==============')    
# PEP8
n = 1
while n <= 3 :  print(n) ; n+=1

print('\n ==============')    
import random
n = random.randrange(0,10)
f = 'no'

print(n)   #taghaloob

while  f == 'no' :
    a = int(input('enter:'))
    
    if a < n :
        print('>')
    elif a > n:
        print('<')
    else:
        print('correct')
        f = 'yes'

print('Thank you.')        
     

















    