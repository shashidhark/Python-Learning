# Maximun/min in list
largest = None
smallest = None
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
	
    if smallest is None or itervar < smallest :
        smallest = itervar

print('Smallest:', smallest)
print('Largest:', largest)
