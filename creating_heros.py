#!/usr/bin/env python3.6

#########################################################
#created by :  br0k3ngl255
#date		: 25.03.2019
#version	:1.0.0
#purpose	:  write a script that creates a list of DC heroes  
#use input functions to ask from user to add all  
#the heroes manually                              
#save the heros in to file called DC_heroes.txt 
##########################################################

###importing libs ::::::::::::::::::::::::::::::::::::::::
import time


##variables  =============================================
hero=''
heroes=[]


while True:
	hero = input('Please insert DC hero name:  (use q to exit)   ')
	if hero != 'q' and hero != "" and hero != " ":
		heroes.append(hero)
	else:
		break
print('thank you - writing data to file')
time.sleep(1)

with open('DC_heroes.txt','a') as f:
	f.write(str(heroes))
	
print('finished writing to file')
