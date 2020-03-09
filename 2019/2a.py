print("Patrick Connolly - Eton College - Age 16\n")
print("British Informatics Olympiad 2019 - Question 2a\n")

# Setup

input = input().split(" ")
maxTrail = int(input[0])
instructions = list(input[1])
numOfMoves = int(input[2])
pos = [0,0]
directions = ["N", "E", "S", "W"]
direction = "N"
trail = []
attempted = []
moves = []
end = False

def is_finished():
    if len(moves) >= numOfMoves:
        return True

def is_stuck():
    if len(attempted) >= 3:
        return True

def is_done():
    if is_finished and is_stuck:
        print("AYAYA")
        return True
    return False

def turn_left(direction):
    index = directions.index(direction)
    if index != 0:
        return directions[index-1]
    else:
        return directions[3]

def turn_right(direction):
    index = directions.index(direction)
    if index != 3:
        direction = directions[index+1]
        return direction
    else:
        direction = directions[0]
        return direction

def set_new_pos(instruction, direction):
    if instruction == "L":
        turn_left(direction)
    elif instruction == "R":
        turn_right(direction)
    if direction == "N":
        return [pos[0], pos[1] + 1]
    elif direction == "E":
        return [pos[0] + 1, pos[1]]
    elif direction == "S":
        return [pos[0], pos[1] - 1]
    else:
        return [pos[0] - 1, pos[1]]

def try_next_instruction(instruction):
    if instruction == "F":
        return "L"
    elif instruction == "L":
        return "R"
    else: 
        return "F"

def move(instruction, direction, pos):
    newPos = set_new_pos(instruction, direction)
    trail.append(pos)
    if newPos not in trail:
        pos = newPos
        print(pos)
        moves.append(pos)
        if is_done:
            return
    else:
        attempted.append(instruction)
        try_next_instruction(instruction)
        if is_done:
            return 

def path():
    for char in instructions:       
        if char == "F":
            print("Moving Forwards")
            move("F", direction, pos)
        elif char == "L":
            print("Moving Left")
            move("L", direction, pos)
        elif char == "R":
            print("Moving Right")
            move("R", direction, pos)
        else:
            print("Invalid instuctions")
        if len(trail) > maxTrail:
            trail.pop(0)


path()
                







