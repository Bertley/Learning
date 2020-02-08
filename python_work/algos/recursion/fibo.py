"""
This deals with Fibonacci numbers which sunflowers, the Golden ratio, fur tree cones, The Da Vinci Code and the song "Lateralus" by Tool have in common. 

The Fibonacci numbers are the numbers of the following sequence of integer values: 

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

The Fibonacci numbers are defined by 

F(n) = F(n-1) + F(n-2)
with F(0) = 0 
and F(1) = 1

The Fibonacci sequence is named after the mathematicia Leonardo of Pisa, who is better known as Fibonacci. 

The Fibonacci numbers are the result of an artificial rabbit population, satisfying the following conditions: 
    - a newly born pair of rabbits, one male, one female, build the initial population
    - these rabbits are able to mate at the age of one month so that at the end of its second month a female can bring forth another pair of rabbits 
    - these rabbits are immortal 
    - a mating pair always produces one new pair (one male, one female) every month from the second month onwards 

The Fibonacci numbers are the numbers of rabbits pairs after n months, i.e after 10 months we have f(10) rabbits. 

"""
# Recursion 

def fib(n): 
    if n == 0: 
        return 0
    elif n == 1: 
        return 1 
    else: 
        return fib(n-1) + fib(n-2)



# Iteration 

def fibi(n): 
    a, b = 0, 1
    for i in range(n): 
        a, b = b, a + b
    return a 


print(fib(5))
print(fibi(3))


