# Write a program which repeatedly reads numbers until the user enters "done". 
# Once "done" is entered, print out the total, count, and average of 
# the numbers. If the user enters anything other than a number, detect 
# their mistake using try and except and print an error message and 
# skip to the next number.
sum = 0
count = 0 
while True:
	val = input('> ')
	if val != 'done':
		try:
			val = int(val)
			count+=1			
			sum+=val
		except:
			print('Invalid data')
	
	else:
		break

avg = sum/count
print('Sum: ', sum, 'Count: ', count, 'Avg: ', avg, sep='\n', end='\n')


# Display max and min or input
max = None
min = None
while True:
	val = input('(Type "done" to exit) >> ')
	if val != 'done':
		try:
			val = int(val)
			if max == None or max < val:
				max = val			
			if min == None or min > val:
				min = val
		except:
			print('Invalid data')
	
	else:
		break

print('Min: ', min, 'Max: ', max, sep='\n', end='\n')


