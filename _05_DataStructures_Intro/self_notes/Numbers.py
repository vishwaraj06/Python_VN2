a=12
b=20
c=18
print(id(a),id(b),id(c))
del a #after deleting variale a,it automatically moves to garbage
print(id(b),id(c))

print("------------------------------------------------")
print(float(b))   # converting int into float
print(complex(b)) # converting  int into complex