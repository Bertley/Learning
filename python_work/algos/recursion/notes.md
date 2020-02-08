# Recursion 

The adjective "recursive" originates from the Latin verb "recurrere", which means "to run back". And this is what a recursive definition or recursive function does: It is "running back" or returning to itself. 

## Factorial 
This defined in mathematical terms as 
```
n! = n * (n-1)!, if n > 1 and f(1) = 1
```

## English example 
The recursive rule allows a phrase to contain an example of itself, as in 
- She thinks that he thinks that they think he knows that she thinks that ... 

The number of sentences is infinite, therefore the number of possible thoughts and intension is infinite too, because every sentence expresses a different thought or intension. 

## Definition 
Recursion is a way of programming a problem, in which a function calls itself one or more times in its body. Usually it's returning the return value of the function call. If the function definition fulfils the condition of recursion, we call this a recursive function. 

### Termination Condition
A recursive function has to terminate to be used in a program. A recursive function terminates, if with every recursive call the solution of the problem is downsized and moved towards to a base case. A base case is a case, where the problem can be solved without further recursion. A recursion can lead to an infinite loop, if the base case is not met in the calls. 

Example: 
```
4! = 4 * 3! 
3! = 3 * 2!
2! = 2 * 1
```
Replacing the calculated values gives us the following expression 
```
4! = 4 * 3 * 2 * 1
```
Generally we can say: Recursion in computer science is a method where the solution to a problem is based on solving smaller instances of the same problem. 