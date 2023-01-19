# Define ENUM

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    
    
# get type of enum
print(type(Color.RED))

# get enam name
print(Color.RED.name)

# get enum value
print(Color.RED.value)

# To compare two members, you can use either is or == operator.

if Color.RED is Color.BLUE:
    print('red is blue')
else:
    print('red is not blue')
    
if Color.RED == 1:
    print('Color.RED == 1')
else:
    print('Color.RED != 1')
    
# Enumeration members are hashable
# Enumeration members are always hashable. It means that you can use the enumeration members as keys in a dictionary or as elements of a Set.

rgb = {
    Color.RED: '#ff0000',
    Color.GREEN: '#00ff00',
    Color.BLUE: '#0000ff'
}

# Get value of key
print(Color['RED'])

# Get key index
print(Color(2))

# compare
print(Color['RED'] == Color(1))

# print by loop
for color in Color:
    print(color)
    
# Enumerations are immutable
# ----------------------------

# Color['YELLOW'] = 4     # will give error