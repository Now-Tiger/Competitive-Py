#!/usr/bin pypy3

# ---------------------- List-Comprehensions in Python ----------------------


# ------- Example without list-comprehension ------- 

sentence = "the quick brown fox jumps over the lazy dog"
# print(sentence)
words = sentence.split()
word_lengths =  []
for word in words :
    if word != 'the' :
        word_lengths.append(len(word))
# print(words)
print(word_lengths)


# ----------- With List-comprehension ------------ 

worldLen = [len(word) for word in words if word != 'the']
print(worldLen)


# ------ Ex.2 ------
#       Using a list comprehension, create a new list 
# called "newlist" out of the list "numbers", 
# which contains only the positive numbers from the 
# list, as integers.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newList = [int(x) for x in numbers if x > 0]
print(newList)

print('-'*30)

# ------ Ex.3 ------
#       Print even and odds array/list of element out of given 
# array of elements 

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 88, .2]

# using list comprehension to get even elements in an array 

even = [i for i in nums if i % 2 == 0]
print(f'This is an array of elements even\n{even}')

# Now store odd elements to an array :
odd = [i for i in nums if i % 2 != 0]
print(f'This is an array of odd elements\n{odd}')