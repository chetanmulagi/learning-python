ans = 5 + 10.0 #type convertion python do auto
print(type(ans)) # int + float its became a float.

ans = int(5+ 10.2) # type casting need to convert manually.
print(type (ans)) # now come type  "int"

val = bool(0)
val2 = bool(10)
print(type(val)) 
print(val, type(val)) # if value 0 means false.
print(val2, type(val2)) # if value non0 means true.