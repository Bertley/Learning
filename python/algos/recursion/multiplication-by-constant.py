"""
Write a recusive version of the function f(n) = 3 * n, i.e. the multiples of 3
"""

def f(n): 
    if n == 0: 
        return 0 
    else:
        return 3 + f(n - 1)


print(f(10))