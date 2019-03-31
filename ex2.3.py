#!/usr/bin/env python3

var = 3
arr = []
per_arr=[1,2,3]

while True:
	if var > 0:
		tmp = input(f'Please enter {var}st string: ')
		arr.append(tmp)
		var -= 1
	else:
		break

print(arr)		
arr.reverse()
print(arr)
arr.pop(1)
arr.insert(1,per_arr)
print(arr)
a,b,c=arr
print(b[1])
