import sys
import os

class Boss(object) : 

	def __init__(self):
		self.name = ""
		self.salary = ""
		print "Boss construtor"

	def setName(self,name):
		self.name = name

	def getName(self):
		return self.name

	def setSalary(self,salary):
		self.salary=salary

	def getSalary(self):
		return self.salary

	def printData(self):
		print self.name," ",self.salary


class Employee(Boss):

	def __init__(self):
		super(Employee,self).__init__()
		print "Employee construtor"


A = Boss()
B = Employee()

A.setName("Vijay")
A.setSalary(1500)

B.setName("Sourav")
B.setSalary(1000)

print A.getName()," ",A.getSalary()
print B.getName()," ",B.getSalary()