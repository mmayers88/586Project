import math

# Initialising hex string
ini_string = "00853a00"

# Printing initial string
print("Initial string", ini_string)

# Code to convert hex to binary
res = "{0:032b}".format(int(ini_string, 16))
l = len(res)
print (l)

# Print the resultant string
print("Resultant string", str(res))