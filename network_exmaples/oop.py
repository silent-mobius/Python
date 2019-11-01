#!/usr/bin/env python3

'''
class Car():
    def __init__(self,brand,year,max_speed):
       self.brand = brand
       self.year = year
       self.max_speed = max_speed
    
    def breaks(self):
        return None

nissan = Car('Nissan',2011,160)

print(nissan.brand, nissan.year,nissan.max_speed,nissan.breaks())
'''

class MyCompany():
    def __init__(self, name, revenue, num_of_employees):
        self.name = name
        self.revenue = revenue
        self.num_of_employees = num_of_employees
    
    def productivity(self):
        return self.revenue,self.num_of_employees,self.name


vaiolabs = MyCompany('VaioLabs', 10 ,2 )
print(vaiolabs.productivity())