# """
# Given a string of words, reverse all the words 

# start = "This is the best"
# finish = "best the is This"

# """

# def reverse(s): 
#     length = len(s)
#     spaces = [' ']
#     words = []
#     i = 0 

#     while  i < length: 
#         if s[i] not in spaces: 
#             word_start = i 

#             while i < length and s[i] not in spaces: 
#                 i += 1

#             words.append(s[word_start:i])

#         i += 1 

#     return " ".join(reversed(s))


# # def reverse(s): 
# #     s = s.split()
# #     s.reverse()
# #     return s 

# # def reverse(s): 
#     # return " ".join(reversed(s.split()))


# # def reverse(s): 
#     # return " * ".join(s.split()[::-1])

# # def reverse(s): 
#     # return s.split()[::-1]


# print(reverse("This is the best"))

# def rev(s):
#     s = s.lower()
#     str = ""
#     for i in s: 
#         str = i + str
#     print(str)



# Using recursion 

def rev(s): 
    if len(s) == 0: 
        return s

    else: 
        return rev(s[1:]) + s[0]


print(rev("Best"))