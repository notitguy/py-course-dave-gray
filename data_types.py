meaning = 42
# Ternary
# print('Right on!') if meaning > 10 else print('Not today')

# constructor function
# pizza = str('Pepperoni')
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

first = 'James'
last = 'Rodriguez'

# concatenation
fullname = first + ' ' + last
fullname += '!'
# print(fullname)

# mutltiine
multiline = '''
Hey there
What u doing?
          All good?
'''
# print(multiline)

# escape spec. charac.

sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
# print(sentence)

#  string methods
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))
