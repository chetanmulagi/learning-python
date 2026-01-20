vars = False

print(not vars) #true
print(not (10 > 15)) # true

# "not" operator  always reverse variables

print((10 > 5) and (5 > 3)) # true
print((10 > 5) and (5 > 8)) # false
print((10 > 15) and (5 > 8)) # false

# when both values true that time only show "and" operator true

print((10 > 5) or (5 > 3)) # true
print((10 > 5) or (5 > 8)) # true
print((10 > 15) or (5 > 8)) # false

# when both values wrong that time only show "or" operator false