list1 = [1,2,3]
list2 = [4,5,6]

print list1+list2
print list1*3
print 3 in list1
print 3 in list2

print "length of the list : "
print len(list1)

list3 = [1,2,3]
print "comparsion of the 2 list : "
print cmp(list1,list2)
print cmp(list2,list1)
print cmp(list1,list3)

print max(list1)
print min(list1)

new_list = []

for i in range(6):
	new_list.append(i)

new_list.append(3)

print new_list.count(3)
print new_list.index(2)
print new_list.pop(0)
print new_list.pop(-1)
print new_list
new_list.remove(5)
new_list.reverse()
print new_list


list4 = [2,3,2,31,1,0]
list4.sort()
print list4