file = open('directions.txt', 'r')
lines = file.readlines()

def part_1():
    total_horizontal_pos = 0
    total_depth = 0

    for line in lines:
        elements = line.split(" ")
        direction = elements[0]
        distance = int(elements[1])
        if direction == "forward":
            total_horizontal_pos += distance
        elif direction == "up":
            total_depth -= distance
        elif direction == "down":
            total_depth += distance

    return total_depth*total_horizontal_pos

def part_2():
    total_horizontal_pos = 0
    total_depth = 0
    total_aim = 0

    for line in lines:
        elements = line.split(" ")
        direction = elements[0]
        distance = int(elements[1])
        if direction == "forward":
            total_horizontal_pos += distance
            total_depth += (total_aim * distance)
        elif direction == "up":
            total_aim -= distance
        elif direction == "down":
            total_aim += distance

    return total_depth*total_horizontal_pos

print("Part 1: " + str(part_1()))
print("Part 2: " + str(part_2()))