def move(a,b): 
    print("Move from {} to {}".format(a,b))

def hanoi(n, initial, auxillary, destination):
    if n == 0: 
        pass 
    else: 
        # Try solving the problem for n-1
        # by using the destination as the helper to move from initial to auxilary.  
        hanoi(n-1, initial, destination, auxillary) 
        # And then move the last one to the destination. 
        move(initial, destination)
        # Then use the intial ad the helper to move n-1 from the auxilary to the destination.
        hanoi(n-1, auxillary, initial, destination)


hanoi(100,'A','B','C')