print("Patrick Connolly - Eton College - Age 16\n")
print("British Informatics Olympiad 2019 - Question 2a\n")

# Setup
global pos
global direction

input = input().split(" ")
maxTrail = input[0]
instructions = list(input[1])
numOfMoves = input[2]
pos = [0,0]
direction = "N"
trail = []

def move_forward():
    if direction == "N":
        pos[1] += 1
    elif direction == "E":
        pos[0] += 1
    elif direction == "S":
        pos[1] -= 1
    elif direction == "W":
        pos[0] -= 1
    else:
        print("Invalid direction")

def move_left():
    if direction == "N":
        direction = "W"
        move_forward()
    elif direction == "E":
        direction = "N"
        move_forward()
    elif direction == "S":
        direction = "E"
        move_forward()
    elif direction == "W":
        direction = "S"
        move_forward()
    else:
        print("Invalid direction")










