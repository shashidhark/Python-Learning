#Program to with exception handler

v1_str = input("Enter value for v1 = ");
v2_str = input("Enter value for v2 = ");

#For v1
try:
        v1_int = int(v1_str)
except:
        print('Expected number for v1, Converting "'+v1_str+'" to 0')
        v1_int = 0;
        
#For v2
try:
        v2_int = int(v2_str)
except:
        print('Expected number for v2, converting "'+v2_str+'" to 0')
        v2_int = 0;

sum = v1_int + v2_int;
print("Sum of "+ str(v1_int) + " and " + str(v2_int) + " is :" + str(sum));
