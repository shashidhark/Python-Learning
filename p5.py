#Built-in functions

val = 32;
end = '\n\n';
#print
print('Value of variable val is '+ str(val), end=end)

#datatype
print('Data type of val is :')
print(type(val), end=end)

val = 'Hello world!!'

#find max/min char (ASCII val)
print('Max char of <'+val+'> is :')
print(max(val), end=end)
print('Min char of <'+val+'> is :')
print(min(val), end=end)

#Length 
print('Length of <'+val+'> is :')
print(len(val), end=end)

#Type conversion
val='32'
val = int(val)
print(type(val), end=end)

val = 'hello'
# val = int(val)
#Error!!

val = str(32)
print(type(val), end=end)

val = str(3.14159)
print(type(val), end=end)

