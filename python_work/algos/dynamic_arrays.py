def anagram(s1,s2): 
    # Remove spaces and change string to lower case

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Check if same number of characters. 
    if len(s1) != len(s2):
        return False

    # count frequency of each letter
    count = {}

    for letter in s1: 
        if letter in count: 
            count[letter] += 1 
        else: 
            count[letter] = 1

    # do the reverse for second string 

    for letter in s2: 
        if letter in count: 
            count[letter] -= 1 
        else: 
            count[letter] = 1

    for k in count: 
        if count[k] != 0: 
            return False
    
    return True
    
print(anagram('dogdfff', 'godggdf'))