# ----------------------------
# Practical example
# ----------------------------

from enum import Enum

class Direction(Enum):
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"
    
def move(direction):
    if not isinstance(direction, Direction):
        raise TypeError('direction must be an instance of Direction Enum')
    
    if direction.value == "left":
        print("Go Left")
    elif direction.value == "right":
        print("Go Right")
    else:
        print("Invalid Character")
        
move(Direction.LEFT)
# move("right")   # will give error