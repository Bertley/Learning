"""

To make fib function faster we can implement a memory since it doesn't remember previously calculated values. 

We do so by using a dictionary to save the previously calculated values. 

"""

def fibm(n, memo = {0:0, 1:1}): 
    if not n in memo: 
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]

print(fibm(5))