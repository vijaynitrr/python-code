import sys
import os

dict = { 'name' : 'vijay' , 'age' : 25 , 'sex' : 'male' } 

print dict

print len(dict)

a = str(dict)
a = a+'vijay'
print a

dict1 = dict.copy()

print dict1

dict1.clear()

print dict1

#get the value
print dict.get('name')

#check that key is available or not
print dict.has_key('name')

#dictionary item , keys and values
print dict.items()
print dict.keys()
print dict.values()

dict['last name']='khandal'

#loop for printing keys and values
for keys,values  in dict.items():
	print "%s has value %s"%(keys,values)