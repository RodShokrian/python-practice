numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [i for i in numbers if i > 0]
print(newlist)
#format for list comprehension:
#[ expression for item in list if conditional ]
#equivalent to:
#for item in list:
#    if conditional:
#        expression


