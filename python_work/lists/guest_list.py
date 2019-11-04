guest_list = ['daddy', 'mommy', 'rose', 'christopher', 'susan', 'bertha', 'jerry', 'ebose', 'ofure']

for guest in guest_list: 
    invite = f"\nHello {guest.title()}, you're cordially invited to my dinner party at kost :)"
    print(invite)
    
# Rose said she cant make it so i need to find her name and take out 
cant_make_it_index = 2
cant_make_it = guest_list.pop(cant_make_it_index)
print(f"\n{cant_make_it.title()} said she can't make it")

# So i'm inviting clement instead 

guest_list.insert(cant_make_it_index, 'clement')

# Sending new invites 

for guest in guest_list: 
    invite = f"\nHello {guest.title()}, you're cordially invited to my dinner party at kost :)"
    print(invite)

# My table just got bigger and i have invite more people 

for guest in guest_list:
    message = f"\nHey {guest.title()}, i just got a bigger table for a larger party :)"
    print(message)

guest_list.insert(0, 'stephen')
guest_list.insert(4, 'harsh')
guest_list.append('olu')

for guest in guest_list: 
    invite = f"\nHello {guest.title()}, you're cordially invited to my dinner party at kost :)"
    print(invite)

print("\nHey you only invite 2 people, you're fucked")

# Now i have to take out 10 people from my list
for i in range(len(guest_list) - 2):
    removed_guess = guest_list.pop()
    print(f"\nHey {removed_guess.title()}, sorry i had to take you off the list")

for guest in guest_list: 
    invite = f"\nHello {guest.title()}, you're cordially invited to my dinner party at kost :)"
    print(invite)

del guest_list[0]
del guest_list[0]

print(guest_list)