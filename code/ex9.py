from sys import argv

a,b = argv

c = open(b)

print c.read()

d = raw_input('enter new filename : ')

e = open(d)

print e.read()