"""
Write a recursive Python function that returns the sum of the first n integers, i.e f(5) = 15
(Hint: The function will be similiar to the factorial function!)
"""

def f(n): 
    if n == 0: 
        return 0 
    else: 
        return n + f(n - 1)


print(f(10))