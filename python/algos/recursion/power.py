"""
pow(2,2) = 4 

"""

def pow(n,y): 
    if y == 0: 
        return 1
    else: 
        return n * pow(n, y-1)

print(pow(2,10))