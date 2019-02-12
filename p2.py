#Program to add two numbers with proper messages

v1 = input("Enter value for v1 = ");
v2 = input("Enter value for v2 = ");

if v1.isdigit() == False:
        print("Value v1 shoult be number, converting to '0'");
        v1 = '0'

if v2.isdigit() == False:
        print("Value v2 should be number, converting to '0'")
        v2 = '0'

sum = int(v1)+int(v2);
print("Sum of "+ v1 + " and " + v2 + " is :" + str(sum));
