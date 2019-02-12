#Program to fetch command line arguments and add

import sys

if len(sys.argv)==3:
        v1 = sys.argv[1]
        v2 = sys.argv[2]
        if v1.isdigit() == False:
                v1 = '0'

        if v2.isdigit() == False:
                v2 = '0'

        sum = int(v1) + int(v2)
        print("Sum of "+v1+" and "+v2+" is :"+str(sum))
else:
        print("Pass 2 integer arguments.")
