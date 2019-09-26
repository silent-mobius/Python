#!/usr/bin/env python3

########################################################################
# created by: Pushtakio
# purpose: practice OOP
# date: unknow
# version: unknow
########################################################################

class Person():
	def __init__(self,name='',lname='',age=0,hght='',wght='',id_num=''):
		self.name=name
		self.lname=lname
		self.age=age
		self.hght=hght
		self.wght=wght
		self.id_num=id_num
		
	def sleep(self,time=0):
		print(f' i will sleep {time} hours')
		
	def eat(self,kg=0):
		if kg <= 0:
			print(f'i\'ll strave to death with {kg} amount of food')
		else:
			print(f'i\'ll be eating {kg} of food')
	
	def walk(self,dinst=0):
		if dinst <= 0:
			print(f'i am lazy so i will walk {dinst} km of distance')
		elif dinst >= 1 and dinst <= 5:
			print(f'i am lazy so i will walk {dinst} km of distance')
		else:
			print(f'feeling in sport mood todat, so i will run {dinst} km today')

	def wake(self,tm=5):
		print(f'i still want to sleep {tm} hours at least')
	
	def work(self,tm=9):
		if tm <= 9:
			print(f'i\'ll be back home in {tm} hours')
		elif tm >= 9:
			print(f'i\'ll be back home in {tm} hours')
		else:
			print(f'not coming back home tonight')
	
	def __repr__(self):
		print(f'this is Person class: {age}{name}{lname}')
	
	def __str__(self):
		print(f'this is Person class: {age}{name}{lname}')


