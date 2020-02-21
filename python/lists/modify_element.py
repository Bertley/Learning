motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)


# Adding elements to a list 

# 1. Appending Elements to the End of a List 

# motorcycles.append('ducatti')
# print(motorcycles) # appends 'ducatti' to the end of the array 

# 2. Inserting Elements into a list 

# motorcycles.insert(0, 'ducatti')
# print(motorcycles) # The insert method opens a space at position 0 and stores the value 'ducatti' at that location.

# 3. Removing elements from a list 

## if you know the position of the item you want to remove from a list, you can use the del statement 

# del motorcycles[0]
# print(motorcycles)

## removing an item using the pop() method 

# popped_motocycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motocycle)

# A use of pop: If the list of motorcycles are a stored in a chronological order according to when we owned them 

# last_owned = motorcycles.pop()
# print(f"The last motorcyle I owned was a {last_owned.title()}.") 

### poping items from any position in a list 

# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}")

### removing an item by value 

# motorcycles.remove('yamaha')
# print(motorcycles)
motorcycles.append('ducatti')
print(motorcycles)
too_expensive = 'ducatti'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")