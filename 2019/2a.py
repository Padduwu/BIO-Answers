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
    else:
        return False

def is_stuck():
    if len(attempted) >= 3:
        return True
    else:
        return False

def is_done():
    if is_finished() or is_stuck():
        return True
    else:
        return False

def turn_left(direction):
    index = directions.index(direction)
    if index != 0:
        direction = directions[index-1]
        return direction
    else:
        direction = directions[3]
        return direction

def turn_right(direction):
    index = directions.index(direction)
    if index != 3:
        direction = directions[index+1]
        return direction
    else:
        direction = directions[0]
        return direction

def set_new_pos(instruction):
    global direction
    if instruction == "L":
        direction = turn_left(direction)
    elif instruction == "R":
        direction = turn_right(direction)
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

def move(instruction, direction):
    global pos
    newPos = set_new_pos(instruction)
    trail.append(pos)
    if newPos not in trail:
        pos = newPos
        print("Position:", pos)
        print("Facing:", direction)
        moves.append(pos)
    else:
        attempted.append(instruction)
        if is_stuck():
            print("Stuck. Ending...")
            return
        move(try_next_instruction(instruction), direction)


def path():
    while True:
        for char in instructions: 
            if is_done():
                return
            if char == "F":
                print("Moving Forwards")
                move("F", direction)
            elif char == "L":
                print("Moving Left")
                move("L", direction)
            elif char == "R":
                print("Moving Right")
                move("R", direction)
            else:
                print("Invalid instuctions")
            if len(trail) > maxTrail:
                trail.pop(0)

path()
                







