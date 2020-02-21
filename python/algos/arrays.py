# How arrays work
# Need to  understand low level computer architecture. 
# Arrays are stored and retrieved in O(1)
# If you index 1 or index another another constanst the programming language is going to know where in the memory
# the index is located. 

# Python represents UNICODE character with 16bits(2bytes)
# 6 character string is going to be stored in 12 bytes. 
# Each character takes up a CELL which is 1byte and 8 bytes. 
# Index describes location. 


# List and References. 

import sys
n=10 
data = []

for i in range(n): 
    a = len(data)
    b = sys.getsizeof(data)
    
    print('Length: {0:3d}; Size in bytes: {1:4d} '.format(a,b))
    
    data.append(n)

