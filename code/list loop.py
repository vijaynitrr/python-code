import string 
import sys

list = []

n = int(raw_input())

for i in range(n) :
	p = raw_input()
	list.append(int(p))

for i in list :
	print "element was : %d "%i
